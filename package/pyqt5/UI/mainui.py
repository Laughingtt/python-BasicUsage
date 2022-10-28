# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # def __init__(self, item_mean_std):
    #     self.item_mean_std = item_mean_std
    #     self.setupUi(MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1645, 954)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 58, 16))
        self.label.setObjectName("label")
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(190, 30, 251, 31))
        self.file_path.setObjectName("file_path")
        self.item_mean_std = QtWidgets.QTableWidget(self.centralwidget)
        self.item_mean_std.setGeometry(QtCore.QRect(20, 80, 500, 192))
        self.item_mean_std.setObjectName("item_mean_std")
        
        #head = ['Special Build Description','mean','median','std']
        self.item_mean_std.setColumnCount(0)
        self.item_mean_std.setRowCount(0)
        #self.item_mean_std.setHorizontalHeaderLabels(head)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.hello)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add CSV"))
        self.label.setText(_translate("MainWindow", "File Path:"))
        self.file_path.setText(_translate("MainWindow", "hi"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # def update_item_mean_std(self):
    #     self.item_mean_std.setRowCount(100)
    #     self.item_mean_std.setColumnCount(4)
        