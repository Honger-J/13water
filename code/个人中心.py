# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '个人中心.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_personcenter(object):
    def setupUi(self, personcenter):
        personcenter.setObjectName("personcenter")
        personcenter.resize(1280, 720)
        personcenter.setMinimumSize(QtCore.QSize(1280, 720))
        personcenter.setMaximumSize(QtCore.QSize(1280, 720))
        personcenter.setStyleSheet("#personcenter{\n"
                                   "border-image: url(:/.../background2.jpg);\n"
                                   "}")
        self.centralwidget = QtWidgets.QWidget(personcenter)
        self.centralwidget.setObjectName("centralwidget")
        self.jiesuan = QtWidgets.QGraphicsView(self.centralwidget)
        self.jiesuan.setGeometry(QtCore.QRect(110, 20, 1050, 680))
        self.jiesuan.setMinimumSize(QtCore.QSize(1050, 680))
        self.jiesuan.setMaximumSize(QtCore.QSize(1050, 680))
        self.jiesuan.setMouseTracking(False)
        self.jiesuan.setTabletTracking(False)
        self.jiesuan.setToolTipDuration(-1)
        self.jiesuan.setStyleSheet("#jiesuan{\n"
                                   "border-image: url(:/.../yangpizhi2.png);\n"
                                   "}")
        self.jiesuan.setLineWidth(0)
        self.jiesuan.setObjectName("jiesuan")
        self.flag = QtWidgets.QGraphicsView(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(565, 80, 150, 550))
        self.flag.setStyleSheet("border-image: url(:/.../qizhi.png);")
        self.flag.setObjectName("flag")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.flag.setGraphicsEffect(op)
        self.flag.setAutoFillBackground(True)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(480, -50, 331, 251))
        self.graphicsView.setStyleSheet("border-image: url(:/.../logo4.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.touxiangkuang = QtWidgets.QGraphicsView(self.centralwidget)
        self.touxiangkuang.setGeometry(QtCore.QRect(187, 77, 116, 116))
        self.touxiangkuang.setMinimumSize(QtCore.QSize(116, 116))
        self.touxiangkuang.setMaximumSize(QtCore.QSize(116, 116))
        self.touxiangkuang.setStyleSheet("#touxiangkuang{\n"
                                         "border-image: url(:/.../touxiangkuang.png);\n"
                                         "}")
        self.touxiangkuang.setObjectName("touxiangkuang")
        self.touxiang = QtWidgets.QGraphicsView(self.centralwidget)
        self.touxiang.setGeometry(QtCore.QRect(190, 80, 110, 110))
        self.touxiang.setMinimumSize(QtCore.QSize(110, 110))
        self.touxiang.setMaximumSize(QtCore.QSize(110, 110))
        self.touxiang.setStyleSheet("#touxiang{\n"
                                    "border-image: url(:/.../touxiang.jpg);\n"
                                    "}")
        self.touxiang.setObjectName("touxiang")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(320, 120, 221, 61))
        self.namelabel.setStyleSheet("font: 30pt \"华文新魏\";")
        self.namelabel.setObjectName("namelabel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 170, 211, 61))
        self.label_4.setStyleSheet("font: 30pt \"华文新魏\";")
        self.label_4.setObjectName("label_4")
        self.history1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.history1.setGeometry(QtCore.QRect(640, 250, 401, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.history1.setFont(font)
        self.history1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.history1.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.history1.setObjectName("history1")
        self.history2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.history2.setGeometry(QtCore.QRect(640, 340, 401, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.history2.setFont(font)
        self.history2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.history2.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.history2.setObjectName("history2")
        self.history3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.history3.setGeometry(QtCore.QRect(640, 430, 401, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.history3.setFont(font)
        self.history3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.history3.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.history3.setObjectName("history3")
        self.history4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.history4.setGeometry(QtCore.QRect(640, 520, 401, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.history4.setFont(font)
        self.history4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.history4.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.history4.setObjectName("history4")
        self.buttonfanhui = QtWidgets.QPushButton(self.centralwidget)
        self.buttonfanhui.setGeometry(QtCore.QRect(980, 610, 118, 44))
        self.buttonfanhui.setMinimumSize(QtCore.QSize(118, 44))
        self.buttonfanhui.setMaximumSize(QtCore.QSize(118, 44))
        self.buttonfanhui.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonfanhui.setTabletTracking(False)
        self.buttonfanhui.setStyleSheet("#buttonfanhui{\n"
                                        "    font: 22pt \"华文新魏\";\n"
                                        "    color:rgb(0, 0, 0);\n"
                                        "    border:none;\n"
                                        "    border-radius:8px;\n"
                                        "    background-color:transparent;\n"
                                        "}")
        self.buttonfanhui.setObjectName("buttonfanhui")
        self.score1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score1.setGeometry(QtCore.QRect(440, 250, 131, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.score1.setFont(font)
        self.score1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score1.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.score1.setObjectName("score1")
        self.score2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score2.setGeometry(QtCore.QRect(440, 340, 131, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.score2.setFont(font)
        self.score2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score2.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.score2.setObjectName("score2")
        self.score3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score3.setGeometry(QtCore.QRect(440, 430, 131, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.score3.setFont(font)
        self.score3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score3.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.score3.setObjectName("score3")
        self.score4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score4.setGeometry(QtCore.QRect(440, 520, 131, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.score4.setFont(font)
        self.score4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score4.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.score4.setObjectName("score4")
        self.ID_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ID_1.setGeometry(QtCore.QRect(210, 250, 171, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.ID_1.setFont(font)
        self.ID_1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID_1.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.ID_1.setObjectName("ID_1")
        self.ID_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ID_2.setGeometry(QtCore.QRect(210, 340, 171, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.ID_2.setFont(font)
        self.ID_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID_2.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.ID_2.setObjectName("ID_2")
        self.ID_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ID_3.setGeometry(QtCore.QRect(210, 430, 171, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.ID_3.setFont(font)
        self.ID_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID_3.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.ID_3.setObjectName("ID_3")
        self.ID_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ID_4.setGeometry(QtCore.QRect(210, 520, 171, 71))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        self.ID_4.setFont(font)
        self.ID_4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID_4.setStyleSheet("background-color: rgba(204, 204, 204,0.3);")
        self.ID_4.setObjectName("ID_4")
        self.jiesuan.raise_()
        self.touxiang.raise_()
        self.touxiangkuang.raise_()
        self.namelabel.raise_()
        self.buttonfanhui.raise_()
        self.ID_1.raise_()
        self.ID_2.raise_()
        self.ID_3.raise_()
        self.ID_4.raise_()
        self.flag.raise_()
        self.label_4.raise_()
        self.graphicsView.raise_()
        self.history1.raise_()
        self.history2.raise_()
        self.history3.raise_()
        self.history4.raise_()
        self.score1.raise_()
        self.score2.raise_()
        self.score3.raise_()
        self.score4.raise_()
        personcenter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(personcenter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        personcenter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(personcenter)
        self.statusbar.setObjectName("statusbar")
        personcenter.setStatusBar(self.statusbar)

        self.retranslateUi(personcenter)
        QtCore.QMetaObject.connectSlotsByName(personcenter)

    def retranslateUi(self, personcenter):
        _translate = QtCore.QCoreApplication.translate
        personcenter.setWindowTitle(_translate("personcenter", "亚瑟王の十三水-个人中心"))
        self.namelabel.setText(_translate("personcenter", "昵称："))
        self.label_4.setText(_translate("personcenter", "历史战局"))
        self.history1.setToolTip(_translate("personcenter", "<html><head/><body><p>出牌情况</p></body></html>"))
        self.history1.setHtml(_translate("personcenter",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt;\"><br /></p></body></html>"))
        self.history2.setToolTip(_translate("personcenter", "<html><head/><body><p>出牌情况</p></body></html>"))
        self.history3.setToolTip(_translate("personcenter", "<html><head/><body><p>出牌情况</p></body></html>"))
        self.history4.setToolTip(_translate("personcenter", "<html><head/><body><p>出牌情况</p></body></html>"))
        self.buttonfanhui.setText(_translate("personcenter", "返回"))
        self.score1.setToolTip(_translate("personcenter", "<html><head/><body><p>得分</p></body></html>"))
        self.score1.setHtml(_translate("personcenter",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.score2.setToolTip(_translate("personcenter", "<html><head/><body><p>得分</p></body></html>"))
        self.score2.setHtml(_translate("personcenter",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.score3.setToolTip(_translate("personcenter", "<html><head/><body><p>得分</p></body></html>"))
        self.score3.setHtml(_translate("personcenter",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.score4.setToolTip(_translate("personcenter", "<html><head/><body><p>得分</p></body></html>"))
        self.score4.setHtml(_translate("personcenter",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ID_1.setToolTip(_translate("personcenter", "<html><head/><body><p>战局ID</p></body></html>"))
        self.ID_1.setHtml(_translate("personcenter",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ID_2.setToolTip(_translate("personcenter", "<html><head/><body><p>战局ID</p></body></html>"))
        self.ID_2.setHtml(_translate("personcenter",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ID_3.setToolTip(_translate("personcenter", "<html><head/><body><p>战局ID</p></body></html>"))
        self.ID_3.setHtml(_translate("personcenter",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ID_4.setToolTip(_translate("personcenter", "<html><head/><body><p>战局ID</p></body></html>"))
        self.ID_4.setHtml(_translate("personcenter",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'华文新魏\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


import IMG
