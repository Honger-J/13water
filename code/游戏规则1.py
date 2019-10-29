# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '游戏规则1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rulewindow1(object):
    def setupUi(self, rulewindow1):
        rulewindow1.setObjectName("rulewindow1")
        rulewindow1.resize(1280, 720)
        rulewindow1.setMinimumSize(QtCore.QSize(1280, 720))
        rulewindow1.setMaximumSize(QtCore.QSize(1280, 720))
        rulewindow1.setStyleSheet("#rulewindow1{border-image: url(:/image/background.png);}")
        self.centralwidget = QtWidgets.QWidget(rulewindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.flag = QtWidgets.QGraphicsView(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(565, 80, 150, 550))
        self.flag.setStyleSheet("border-image: url(:/.../qizhi.png);")
        self.flag.setObjectName("flag")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.flag.setGraphicsEffect(op)
        self.flag.setAutoFillBackground(True)
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
        self.nextpage = QtWidgets.QPushButton(self.centralwidget)
        self.nextpage.setGeometry(QtCore.QRect(950, 610, 161, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(22)
        self.nextpage.setFont(font)
        self.nextpage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextpage.setFlat(True)
        self.nextpage.setObjectName("nextpage")
        rulewindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rulewindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        rulewindow1.setMenuBar(self.menubar)

        self.retranslateUi(rulewindow1)
        QtCore.QMetaObject.connectSlotsByName(rulewindow1)

    def retranslateUi(self, rulewindow1):
        _translate = QtCore.QCoreApplication.translate
        rulewindow1.setWindowTitle(_translate("rulewindow1", "亚瑟王の十三水-游戏规则"))
        self.label_3.setText(_translate("rulewindow1", "        这是一个古老的游戏。大不列颠国王亚瑟·潘德拉贡时常和他的骑士们\n"
                                                       "在圆桌上打十三水…………\n"
                                                       "\n"
                                                       "【规则概括】\n"
                                                       "将一副牌 52 张（即无大小鬼牌）均给四位玩家，每位玩家将 13 张牌分成三\n"
                                                       "组（墩），其中头墩 3 张，中墩 5 张，底墩 5 张，称为前、中、后墩，之后\n"
                                                       "与其它三家比牌型、牌面。较大则为赢一墩。不同的特殊牌型则有额外的墩\n"
                                                       "数计算。\n"
                                                       "【游戏流程】\n"
                                                       "I. 墩牌\n"
                                                       "        在时限内，打出（前墩 3 张，中墩 5 张，后墩 5 张）的对战阵容，三墩\n"
                                                       "牌的牌型必须符合后墩牌型大于或等于中墩牌型，中墩牌型大于或等于前墩\n"
                                                       "牌型。十三水的规则是前墩要比中墩小，而中墩要比后墩小，譬如前墩是一\n"
                                                       "个对子，中墩是一个顺子，后墩是一个葫芦。如果组牌时排错，把葫芦放到\n"
                                                       "第二墩，把顺子放到第三墩，造成第二墩比第三墩大的话，就称为相公，这\n"
                                                       "时要调整回来才能比牌。\n"
                                                       "II．比牌\n"
                                                       "        所有玩家都墩好牌之后，大家翻开牌墩，两两进行比较，假设玩家为"))
        self.nextpage.setText(_translate("rulewindow1", "下一页"))


import backpict
