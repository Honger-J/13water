# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '出牌成功.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Success(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        self.button_return = QtWidgets.QPushButton(Dialog)
        self.button_return.setGeometry(QtCore.QRect(130, 140, 140, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.button_return.setFont(font)
        self.button_return.setObjectName("return_to_register")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 140, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_return.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "提交成功！"))
