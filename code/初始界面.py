# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '初始界面.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstwindow(object):
    def setupUi(self, firstwindow):
        firstwindow.setObjectName("firstwindow")
        firstwindow.resize(1280, 720)
        firstwindow.setMinimumSize(QtCore.QSize(1280, 720))
        firstwindow.setMaximumSize(QtCore.QSize(1280, 720))
        firstwindow.setStyleSheet("#firstwindow{\n"
"border-image: url(:/image/background.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(firstwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dian_ci_jin_ru = QtWidgets.QPushButton(self.centralwidget)
        self.dian_ci_jin_ru.setGeometry(QtCore.QRect(450, 550, 381, 111))
        font = QtGui.QFont()
        font.setFamily("哥特式字体")
        font.setPointSize(48)
        self.dian_ci_jin_ru.setFont(font)
        self.dian_ci_jin_ru.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dian_ci_jin_ru.setStyleSheet("color: rgb(228, 228, 228);\nborder:none;")
        self.dian_ci_jin_ru.setFlat(True)
        self.dian_ci_jin_ru.setObjectName("dian_ci_jin_ru")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, -100, 591, 401))
        self.label.setStyleSheet("border-image: url(:/image/logo4.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.dian_ci_jin_ru.raise_()
        firstwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(firstwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        firstwindow.setMenuBar(self.menubar)

        self.retranslateUi(firstwindow)
        QtCore.QMetaObject.connectSlotsByName(firstwindow)

    def retranslateUi(self, firstwindow):
        _translate = QtCore.QCoreApplication.translate
        firstwindow.setWindowTitle(_translate("firstwindow", "亚瑟王の十三水"))
        self.dian_ci_jin_ru.setText(_translate("firstwindow", "点此进入"))
import backpict
