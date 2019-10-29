# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '排行榜.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ranklist(object):
    def setupUi(self, ranklist):
        ranklist.setObjectName("ranklist")
        ranklist.resize(1280, 720)
        ranklist.setMinimumSize(QtCore.QSize(1280, 720))
        ranklist.setMaximumSize(QtCore.QSize(1280, 720))
        ranklist.setStyleSheet("#ranklist{\n"
                               "border-image: url(:/.../background2.jpg);\n"
                               "}")
        self.centralwidget = QtWidgets.QWidget(ranklist)
        self.centralwidget.setObjectName("centralwidget")
        self.jiesuan = QtWidgets.QGraphicsView(self.centralwidget)
        self.jiesuan.setGeometry(QtCore.QRect(115, 20, 1050, 680))
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
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(480, -50, 331, 251))
        self.graphicsView.setStyleSheet("border-image: url(:/.../logo4.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.buttonfanhui = QtWidgets.QPushButton(self.centralwidget)
        self.buttonfanhui.setGeometry(QtCore.QRect(960, 610, 118, 44))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 120, 281, 81))
        font = QtGui.QFont()
        font.setFamily("哥特式字体")
        font.setPointSize(40)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setObjectName("label")
        self.name1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(340, 210, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name1.setFont(font)
        self.name1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.name1.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                 "font: 36pt \"华文新魏\";")
        self.name1.setObjectName("name1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 220, 101, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 310, 121, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 400, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 490, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 580, 121, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.score1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score1.setGeometry(QtCore.QRect(710, 210, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score1.setFont(font)
        self.score1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score1.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                  "font: 36pt \"华文新魏\";")
        self.score1.setObjectName("score1")
        self.flag = QtWidgets.QGraphicsView(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(565, 80, 150, 550))
        self.flag.setStyleSheet("border-image: url(:/.../qizhi.png);")
        self.flag.setObjectName("flag")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.flag.setGraphicsEffect(op)
        self.flag.setAutoFillBackground(True)
        self.name2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.name2.setGeometry(QtCore.QRect(340, 300, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name2.setFont(font)
        self.name2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.name2.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                 "font: 36pt \"华文新魏\";")
        self.name2.setObjectName("name2")
        self.score2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score2.setGeometry(QtCore.QRect(710, 300, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score2.setFont(font)
        self.score2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score2.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                  "font: 36pt \"华文新魏\";")
        self.score2.setObjectName("score2")
        self.name3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.name3.setGeometry(QtCore.QRect(340, 390, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name3.setFont(font)
        self.name3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.name3.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                 "font: 36pt \"华文新魏\";")
        self.name3.setObjectName("name3")
        self.score3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score3.setGeometry(QtCore.QRect(710, 390, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score3.setFont(font)
        self.score3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score3.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                  "font: 36pt \"华文新魏\";")
        self.score3.setObjectName("score3")
        self.name4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.name4.setGeometry(QtCore.QRect(340, 480, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name4.setFont(font)
        self.name4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.name4.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                 "font: 36pt \"华文新魏\";")
        self.name4.setObjectName("name4")
        self.score4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score4.setGeometry(QtCore.QRect(710, 480, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score4.setFont(font)
        self.score4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score4.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                  "font: 36pt \"华文新魏\";")
        self.score4.setObjectName("score4")
        self.name5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.name5.setGeometry(QtCore.QRect(340, 570, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name5.setFont(font)
        self.name5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.name5.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                 "font: 36pt \"华文新魏\";")
        self.name5.setObjectName("name5")
        self.score5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.score5.setGeometry(QtCore.QRect(710, 570, 231, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.score5.setFont(font)
        self.score5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.score5.setStyleSheet("background-color: rgba(204, 204, 204,0.3);\n"
                                  "font: 36pt \"华文新魏\";")
        self.score5.setObjectName("score5")
        self.jiesuan.raise_()
        self.buttonfanhui.raise_()
        self.label.raise_()
        self.name1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.score1.raise_()
        self.flag.raise_()
        self.graphicsView.raise_()
        self.name2.raise_()
        self.score2.raise_()
        self.name3.raise_()
        self.score3.raise_()
        self.name4.raise_()
        self.score4.raise_()
        self.name5.raise_()
        self.score5.raise_()
        ranklist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ranklist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        ranklist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ranklist)
        self.statusbar.setObjectName("statusbar")
        ranklist.setStatusBar(self.statusbar)

        self.retranslateUi(ranklist)
        QtCore.QMetaObject.connectSlotsByName(ranklist)

    def retranslateUi(self, ranklist):
        _translate = QtCore.QCoreApplication.translate
        ranklist.setWindowTitle(_translate("ranklist", "亚瑟王の十三水-排行榜"))
        self.buttonfanhui.setText(_translate("ranklist", "返回"))
        self.label.setText(_translate("ranklist", "全服前五强"))
        self.name1.setHtml(_translate("ranklist",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("ranklist", "1 ST"))
        self.label_3.setText(_translate("ranklist", "2ND"))
        self.label_4.setText(_translate("ranklist", "3RD"))
        self.label_5.setText(_translate("ranklist", "4TH"))
        self.label_6.setText(_translate("ranklist", "5TH"))
        self.score1.setHtml(_translate("ranklist",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><br /></p></body></html>"))
        self.name2.setHtml(_translate("ranklist",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p></body></html>"))
        self.score2.setHtml(_translate("ranklist",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><br /></p></body></html>"))
        self.name3.setHtml(_translate("ranklist",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p></body></html>"))
        self.score3.setHtml(_translate("ranklist",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><br /></p></body></html>"))
        self.name4.setHtml(_translate("ranklist",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p></body></html>"))
        self.score4.setHtml(_translate("ranklist",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><br /></p></body></html>"))
        self.name5.setHtml(_translate("ranklist",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                      "text-indent:0px;\"><br /></p></body></html>"))
        self.score5.setHtml(_translate("ranklist",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'华文新魏\'; font-size:20pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><br /></p></body></html>"))


import IMG
