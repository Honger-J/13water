# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游戏规则2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rulewindow2(object):
    def setupUi(self, rulewindow2):
        rulewindow2.setObjectName("rulewindow2")
        rulewindow2.resize(1280, 720)
        rulewindow2.setMinimumSize(QtCore.QSize(1280, 720))
        rulewindow2.setMaximumSize(QtCore.QSize(1280, 720))
        rulewindow2.setStyleSheet("#rulewindow2{border-image: url(:/image/background.png);}")
        self.centralwidget = QtWidgets.QWidget(rulewindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(115, 20, 1050, 680))
        self.label.setStyleSheet("border-image: url(:/image/yangpizhi2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, -50, 331, 251))
        self.label_2.setStyleSheet("border-image: url(:/image/logo4.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.flag = QtWidgets.QGraphicsView(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(565, 80, 150, 550))
        self.flag.setStyleSheet("border-image: url(:/.../qizhi.png);")
        self.flag.setObjectName("flag")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.flag.setGraphicsEffect(op)
        self.flag.setAutoFillBackground(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 80, 901, 551))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(950, 610, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(22)
        self.return_2.setFont(font)
        self.return_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_2.setFlat(True)
        self.return_2.setObjectName("return_2")
        rulewindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rulewindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        rulewindow2.setMenuBar(self.menubar)

        self.retranslateUi(rulewindow2)
        QtCore.QMetaObject.connectSlotsByName(rulewindow2)

    def retranslateUi(self, rulewindow2):
        _translate = QtCore.QCoreApplication.translate
        rulewindow2.setWindowTitle(_translate("rulewindow2", "亚瑟王の十三水-游戏规则"))
        self.label_3.setText(_translate("rulewindow2", "\n"
                                                       "甲、乙、丙、丁四位，则甲乙、甲丙、甲丁、乙丙、乙丁、丙丁分别比牌，\n"
                                                       "各家以（前墩对前墩），（中墩对中墩），（后墩对后墩）的方式定出三项\n"
                                                       "胜负关系，再依照这三项胜负关系来判定输赢。\n"
                                                       "        赢一墩：甲的某一墩比乙的对应的墩大，则甲赢 1 水。\n"
                                                       "        输一墩：甲的某一墩比乙的对应的墩小，则甲输 1 水。\n"
                                                       "        平分秋色：甲的某一墩和乙的对应的墩一样大，则甲乙平分秋色。\n"
                                                       "III．特殊比牌\n"
                                                       "        如果玩家能拿到特殊牌型，那么该玩家不参与一般的比牌，而是在其他\n"
                                                       "的玩家的一般比牌结束后，翻开自己的牌。说明: 如果有三家以上拿到特殊\n"
                                                       "牌型，那么系统直接进入特殊比牌阶段，另外一个拿到一般牌型的玩家算\n"
                                                       "输。\n"
                                                       "【胜数计算】\n"
                                                       "        比牌结束后，如果其中一位玩家三墩全部胜过另一位玩家，则称为打\n"
                                                       "枪，该玩家计分翻倍。如果一位玩家和另外一位玩家相比，1 胜 2 和，或 2 \n"
                                                       "胜 1 和，称为辗过，视同打枪。如果其中一位玩家三墩赢过另外三位玩家所\n"
                                                       "有的牌，称通杀，该玩家计分翻倍。\n"
                                                       ""))
        self.return_2.setText(_translate("rulewindow2", "返回"))


import backpict
