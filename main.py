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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
