# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '用户名已被使用.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_account_used(object):
    def setupUi(self, account_used):
        account_used.setObjectName("account_used")
        account_used.resize(400, 300)
        account_used.setMinimumSize(QtCore.QSize(400, 300))
        account_used.setMaximumSize(QtCore.QSize(400, 300))
        self.return_to_register = QtWidgets.QPushButton(account_used)
        self.return_to_register.setGeometry(QtCore.QRect(120, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_to_register.setFont(font)
        self.return_to_register.setObjectName("return_to_register")
        self.label = QtWidgets.QLabel(account_used)
        self.label.setGeometry(QtCore.QRect(80, 60, 241, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(account_used)
        QtCore.QMetaObject.connectSlotsByName(account_used)

    def retranslateUi(self, account_used):
        _translate = QtCore.QCoreApplication.translate
        account_used.setWindowTitle(_translate("account_used", "Dialog"))
        self.return_to_register.setText(_translate("account_used", "返回"))
        self.label.setText(_translate("account_used", "用户名已被使用"))
