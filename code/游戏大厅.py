# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游戏大厅.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_hall(object):
    def setupUi(self, game_hall):
        game_hall.setObjectName("game_hall")
        game_hall.resize(1280, 720)
        game_hall.setMinimumSize(QtCore.QSize(1280, 720))
        game_hall.setMaximumSize(QtCore.QSize(1280, 720))
        game_hall.setStyleSheet("#game_hall{\n"
                                "    \n"
                                "    border-image: url(:/image/background.png);\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(game_hall)
        self.centralwidget.setObjectName("centralwidget")
        self.kai_shi_you_xi = QtWidgets.QPushButton(self.centralwidget)
        self.kai_shi_you_xi.setGeometry(QtCore.QRect(510, 170, 211, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kai_shi_you_xi.setFont(font)
        self.kai_shi_you_xi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kai_shi_you_xi.setStyleSheet("font: 24pt \"华文新魏\";\n"
                                          "    color: rgb(255, 255, 0);\n"
                                          "    border:none;\n"
                                          "    border-radius:8px;\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(234, 11, 11, 255));\n"
                                          "")
        self.kai_shi_you_xi.setFlat(True)
        self.kai_shi_you_xi.setObjectName("kai_shi_you_xi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -20, 1201, 711))
        self.label.setStyleSheet("border-image: url(:/image/game_hall_sword.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ge_ren_zhong_xin = QtWidgets.QPushButton(self.centralwidget)
        self.ge_ren_zhong_xin.setGeometry(QtCore.QRect(510, 270, 211, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ge_ren_zhong_xin.setFont(font)
        self.ge_ren_zhong_xin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ge_ren_zhong_xin.setStyleSheet("font: 24pt \"华文新魏\";\n"
                                            "    color: rgb(255, 255, 0);\n"
                                            "    border:none;\n"
                                            "    border-radius:8px;\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(234, 11, 11, 255));\n"
                                            "")
        self.ge_ren_zhong_xin.setFlat(True)
        self.ge_ren_zhong_xin.setObjectName("ge_ren_zhong_xin")
        self.you_xi_gui_ze = QtWidgets.QPushButton(self.centralwidget)
        self.you_xi_gui_ze.setGeometry(QtCore.QRect(510, 370, 211, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.you_xi_gui_ze.setFont(font)
        self.you_xi_gui_ze.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.you_xi_gui_ze.setStyleSheet("font: 24pt \"华文新魏\";\n"
                                         "    color: rgb(255, 255, 0);\n"
                                         "    border:none;\n"
                                         "    border-radius:8px;\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(234, 11, 11, 255));\n"
                                         "")
        self.you_xi_gui_ze.setFlat(True)
        self.you_xi_gui_ze.setObjectName("you_xi_gui_ze")
        self.pai_hang_bang = QtWidgets.QPushButton(self.centralwidget)
        self.pai_hang_bang.setGeometry(QtCore.QRect(510, 470, 211, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pai_hang_bang.setFont(font)
        self.pai_hang_bang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pai_hang_bang.setStyleSheet("font: 24pt \"华文新魏\";\n"
                                         "    color: rgb(255, 255, 0);\n"
                                         "    border:none;\n"
                                         "    border-radius:8px;\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(234, 11, 11, 255));\n"
                                         "")
        self.pai_hang_bang.setFlat(True)
        self.pai_hang_bang.setObjectName("pai_hang_bang")
        self.label.raise_()
        self.kai_shi_you_xi.raise_()
        self.ge_ren_zhong_xin.raise_()
        self.you_xi_gui_ze.raise_()
        self.pai_hang_bang.raise_()
        game_hall.setCentralWidget(self.centralwidget)

        self.retranslateUi(game_hall)
        QtCore.QMetaObject.connectSlotsByName(game_hall)

    def retranslateUi(self, game_hall):
        _translate = QtCore.QCoreApplication.translate
        game_hall.setWindowTitle(_translate("game_hall", "亚瑟王の十三水"))
        self.kai_shi_you_xi.setText(_translate("game_hall", "开始游戏"))
        self.ge_ren_zhong_xin.setText(_translate("game_hall", "个人中心"))
        self.you_xi_gui_ze.setText(_translate("game_hall", "游戏规则"))
        self.pai_hang_bang.setText(_translate("game_hall", "排行榜"))


import backpict
