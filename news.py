# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'news.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewsWindow(object):
    def setupUi(self, NewsWindow):
        NewsWindow.setObjectName("NewsWindow")
        NewsWindow.resize(726, 599)
        self.centralwidget = QtWidgets.QWidget(NewsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 170, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 621, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 450, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        NewsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain_Window = QtWidgets.QMenu(self.menubar)
        self.menuMain_Window.setObjectName("menuMain_Window")
        NewsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewsWindow)
        self.statusbar.setObjectName("statusbar")
        NewsWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(NewsWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMain_Window.addAction(self.actionExit)
        self.menubar.addAction(self.menuMain_Window.menuAction())

        self.retranslateUi(NewsWindow)
        QtCore.QMetaObject.connectSlotsByName(NewsWindow)

    def retranslateUi(self, NewsWindow):
        _translate = QtCore.QCoreApplication.translate
        NewsWindow.setWindowTitle(_translate("NewsWindow", "MainWindow"))
        self.label_2.setText(_translate("NewsWindow", "Top Headlines:"))
        self.label_3.setText(_translate("NewsWindow", "Description"))
        self.pushButton.setText(_translate("NewsWindow", "Next "))
        self.pushButton_2.setText(_translate("NewsWindow", "Go Back"))
        self.menuMain_Window.setTitle(_translate("NewsWindow", "Main Window"))
        self.actionExit.setText(_translate("NewsWindow", "Exit"))

