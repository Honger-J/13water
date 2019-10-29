# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '教务处认证失败.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jwc_failed(object):
    def setupUi(self, jwc_failed):
        jwc_failed.setObjectName("jwc_failed")
        jwc_failed.resize(400, 300)
        jwc_failed.setMinimumSize(QtCore.QSize(400, 300))
        jwc_failed.setMaximumSize(QtCore.QSize(400, 300))
        self.return_to_register = QtWidgets.QPushButton(jwc_failed)
        self.return_to_register.setGeometry(QtCore.QRect(120, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_to_register.setFont(font)
        self.return_to_register.setObjectName("return_to_register")
        self.label = QtWidgets.QLabel(jwc_failed)
        self.label.setGeometry(QtCore.QRect(80, 60, 241, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(jwc_failed)
        QtCore.QMetaObject.connectSlotsByName(jwc_failed)

    def retranslateUi(self, jwc_failed):
        _translate = QtCore.QCoreApplication.translate
        jwc_failed.setWindowTitle(_translate("jwc_failed", "Dialog"))
        self.return_to_register.setText(_translate("jwc_failed", "返回"))
        self.label.setText(_translate("jwc_failed", "教务处认证失败"))
