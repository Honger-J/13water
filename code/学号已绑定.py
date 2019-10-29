# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '学号已绑定.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stunum_used(object):
    def setupUi(self, stunum_used):
        stunum_used.setObjectName("stunum_used")
        stunum_used.resize(400, 300)
        stunum_used.setMinimumSize(QtCore.QSize(400, 300))
        stunum_used.setMaximumSize(QtCore.QSize(400, 300))
        self.return_to_register = QtWidgets.QPushButton(stunum_used)
        self.return_to_register.setGeometry(QtCore.QRect(120, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.return_to_register.setFont(font)
        self.return_to_register.setObjectName("return_to_register")
        self.label = QtWidgets.QLabel(stunum_used)
        self.label.setGeometry(QtCore.QRect(110, 60, 171, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(stunum_used)
        QtCore.QMetaObject.connectSlotsByName(stunum_used)

    def retranslateUi(self, stunum_used):
        _translate = QtCore.QCoreApplication.translate
        stunum_used.setWindowTitle(_translate("stunum_used", "Dialog"))
        self.return_to_register.setText(_translate("stunum_used", "返回"))
        self.label.setText(_translate("stunum_used", "学号已绑定"))
