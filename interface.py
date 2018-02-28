# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pg_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.pg_bar.setGeometry(QtCore.QRect(50, 510, 691, 23))
        self.pg_bar.setProperty("value", 24)
        self.pg_bar.setObjectName("pg_bar")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(50, 430, 111, 51))
        self.bt_download.setObjectName("bt_download")
        self.bt_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.bt_cancel.setGeometry(QtCore.QRect(190, 430, 111, 51))
        self.bt_cancel.setObjectName("bt_cancel")
        self.f_imageVideo = QtWidgets.QFrame(self.centralwidget)
        self.f_imageVideo.setGeometry(QtCore.QRect(50, 30, 231, 161))
        self.f_imageVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_imageVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_imageVideo.setObjectName("f_imageVideo")
        self.text_videoDescription = QtWidgets.QTextEdit(self.centralwidget)
        self.text_videoDescription.setGeometry(QtCore.QRect(300, 30, 411, 161))
        self.text_videoDescription.setObjectName("text_videoDescription")
        self.listview_videos = QtWidgets.QListView(self.centralwidget)
        self.listview_videos.setGeometry(QtCore.QRect(50, 211, 661, 131))
        self.listview_videos.setObjectName("listview_videos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 430, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 370, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 370, 531, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Descargar"))
        self.bt_cancel.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "ARCH MUSIC"))
        self.label_2.setText(_translate("MainWindow", "Path del fichero"))

