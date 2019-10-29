# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录反馈1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_feedback1(object):
    def setupUi(self, login_feedback1):
        login_feedback1.setObjectName("login_feedback1")
        login_feedback1.resize(400, 300)
        login_feedback1.setMinimumSize(QtCore.QSize(400, 300))
        login_feedback1.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(login_feedback1)
        self.label.setGeometry(QtCore.QRect(60, 50, 271, 41))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.return_2 = QtWidgets.QPushButton(login_feedback1)
        self.return_2.setGeometry(QtCore.QRect(140, 190, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_2.setFont(font)
        self.return_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_2.setFlat(False)
        self.return_2.setObjectName("return_2")

        self.retranslateUi(login_feedback1)
        QtCore.QMetaObject.connectSlotsByName(login_feedback1)

    def retranslateUi(self, login_feedback1):
        _translate = QtCore.QCoreApplication.translate
        login_feedback1.setWindowTitle(_translate("login_feedback1", "Dialog"))
        self.label.setText(_translate("login_feedback1", "用户名或密码错误"))
        self.return_2.setText(_translate("login_feedback1", "返回"))
