# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ground = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.ground.setObjectName("ground")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ground)
        self.grained = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.grained.setObjectName("grained")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.grained)
        self.degree = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.degree.setMinimum(1)
        self.degree.setMaximum(5)
        self.degree.setObjectName("degree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.degree)
        self.type = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.type.setObjectName("type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.type)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price.setObjectName("price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price)
        self.package_size = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.package_size.setObjectName("package_size")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.package_size)
        self.taste = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.taste.setObjectName("taste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 260, 241, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена за упаковку (в рублях)"))
        self.ground.setText(_translate("MainWindow", "Молотый"))
        self.grained.setText(_translate("MainWindow", "В зёрнах"))
        self.label_3.setText(_translate("MainWindow", "Размер упаковки (в граммах)"))
        self.pushButton.setText(_translate("MainWindow", "Отредактировать"))