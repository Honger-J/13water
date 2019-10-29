# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '超时.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_overtime(object):
    def setupUi(self, overtime):
        overtime.setObjectName("overtime")
        overtime.resize(400, 300)
        overtime.setMinimumSize(QtCore.QSize(400, 300))
        overtime.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(overtime)
        self.label.setGeometry(QtCore.QRect(150, 40, 81, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.return_2 = QtWidgets.QPushButton(overtime)
        self.return_2.setGeometry(QtCore.QRect(130, 200, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_2.setFont(font)
        self.return_2.setObjectName("return_2")

        self.retranslateUi(overtime)
        QtCore.QMetaObject.connectSlotsByName(overtime)

    def retranslateUi(self, overtime):
        _translate = QtCore.QCoreApplication.translate
        overtime.setWindowTitle(_translate("overtime", "Dialog"))
        self.label.setText(_translate("overtime", "超时"))
        self.return_2.setText(_translate("overtime", "返回"))
