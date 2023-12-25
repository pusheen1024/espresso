import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.select_data)
        self.addButton.clicked.connect(self.add_data)
        self.editButton.clicked.connect(self.edit_data)

    def select_data(self):
        self.tableWidget.clear()
        degree = f'degree = {self.degree.text()}' if self.degree.text() else 'TRUE'
        if self.grained.isChecked() and not self.ground.isChecked():
            structure = 'structure.id = 0'
        elif not self.grained.isChecked() and self.ground.isChecked():
            structure = 'structure.id = 1'
        else:
            structure = 'TRUE'
        price = f'price {self.price.text()}' if self.price.text() else 'TRUE'
        package_size = f'package_size {self.package_size.text()}' if self.package_size.text() else 'TRUE'

        query = f'''SELECT coffee.id, type, degree, structure.name, taste, price, package_size
FROM coffee LEFT JOIN structure ON coffee.structure = structure.id
WHERE {degree} AND {structure} AND {price} AND {package_size}'''
        result = self.cur.execute(query).fetchall()

        if not result:
            self.statusbar.showMessage('Ничего не найдено!')
        else:
            headers = ['ID', 'Сорт', 'Степень обжарки', 'Структура', 'Описание вкуса', 'Цена', 'Размер упаковки']
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(headers))
            self.tableWidget.setHorizontalHeaderLabels(headers)
            for i, row in enumerate(result):
                for j, item in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
            self.statusbar.showMessage('')

    def add_data(self):
        self.statusbar.showMessage('')
        self.add_coffee_widget = addEditCoffeeForm(self)
        self.add_coffee_widget.show()

    def edit_data(self):
            selected = self.tableWidget.selectedItems()
            if selected:
                self.edit_coffee_widget = addEditCoffeeForm(self,
                                                            int(self.tableWidget.item(selected[0].row(), 0).text()))
                self.edit_coffee_widget.show()
            else:
                self.statusbar.showMessage('Ничего не выбрано.')


class addEditCoffeeForm(QMainWindow):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.ground.setChecked(True)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        if coffee_id is not None:
            self.coffee_id = coffee_id
            self.pushButton.clicked.connect(self.edit_elem)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            self.get_elem()
        else:
            self.pushButton.clicked.connect(self.add_elem)
            self.pushButton.setText('Добавить')
            self.setWindowTitle('Добавление записи')

    def get_verdict(self):
        try:
            self.type_value = self.type.text()
            if not self.type_value:
                raise ValueError
            self.degree_value = self.degree.value()
            self.structure_value = int(self.ground.isChecked())
            self.taste_value = self.taste.toPlainText()
            self.price_value = int(self.price.text())
            self.package_size_value = int(self.package_size.text())
            return True
        except ValueError:
            return False

    def add_elem(self):
        if self.get_verdict():
            self.statusbar.showMessage('')
            self.cur.execute('''INSERT INTO coffee(id, type, degree, structure, taste, price, package_size) 
VALUES (?, ?, ?, ?, ?, ?, ?)''',
                             [self.get_new_id(), self.type_value, self.degree_value, self.structure_value,
                              self.taste_value, self.price_value, self.package_size_value])
            self.con.commit()
            self.parent().select_data()
            self.close()
        else:
            self.statusbar.showMessage('Добавление записи невозможно.')

    def edit_elem(self):
        if self.get_verdict():
            self.statusbar.showMessage('')
            self.cur.execute('''UPDATE coffee SET type = ?, degree = ?, structure = ?, 
taste = ?, price = ?, package_size = ? WHERE id = ?''',
                             [self.type_value, self.degree_value, self.structure_value,
                              self.taste_value, self.price_value, self.package_size_value, self.coffee_id])
            self.con.commit()
            self.parent().select_data()
            self.close()
        else:
            self.statusbar.showMessage('Редактирование записи невозможно.')

    def get_elem(self):
        query = f'SELECT coffee.id, type, degree, structure, taste, price, package_size FROM coffee WHERE coffee.id = ?'
        result = self.cur.execute(query, [self.coffee_id]).fetchall()
        _, type_value, degree_value, structure_value, taste_value, price_value, package_size_value = result[0]
        self.type.setText(type_value)
        self.degree.setValue(degree_value)
        self.grained.setChecked(not structure_value)
        self.ground.setChecked(structure_value)
        self.taste.setPlainText(taste_value)
        self.price.setText(str(price_value))
        self.package_size.setText(str(package_size_value))

    def get_new_id(self):
        # Because of some problems with auto-increment
        result = self.cur.execute('SELECT id FROM coffee').fetchall()
        return max(result)[0] + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
