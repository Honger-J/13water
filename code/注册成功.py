# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '注册成功.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_success(object):
    def setupUi(self, register_success):
        register_success.setObjectName("register_success")
        register_success.resize(400, 300)
        register_success.setMinimumSize(QtCore.QSize(400, 300))
        register_success.setMaximumSize(QtCore.QSize(400, 300))
        self.return_to_login = QtWidgets.QPushButton(register_success)
        self.return_to_login.setGeometry(QtCore.QRect(120, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_to_login.setFont(font)
        self.return_to_login.setObjectName("return_to_login")
        self.label = QtWidgets.QLabel(register_success)
        self.label.setGeometry(QtCore.QRect(120, 60, 131, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(register_success)
        QtCore.QMetaObject.connectSlotsByName(register_success)

    def retranslateUi(self, register_success):
        _translate = QtCore.QCoreApplication.translate
        register_success.setWindowTitle(_translate("register_success", "Dialog"))
        self.return_to_login.setText(_translate("register_success", "返回登录"))
        self.label.setText(_translate("register_success", "注册成功"))
