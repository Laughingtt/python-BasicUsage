from PyQt5 import QtWidgets
import sys


import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout, QTableWidgetItem, QComboBox,QFrame


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mainui import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):



	def __init__(self):
		super(mywindow,self).__init__()
		self.setupUi(self)



	def update_item_mean_std(self):
		temp_data = pd.read_csv('/Users/willzhang/Desktop/py/pdata/cpk.csv', header=0)
		column =4
		row= temp_data.count().values[0]
		head = ['Special Build Description', 'mean', 'median', 'std']
		self.item_mean_std.setColumnCount(column)
		self.item_mean_std.setRowCount(row)
		self.item_mean_std.setHorizontalHeaderLabels(head)
		for i in range(0,row):
			for j in range(0, column):
				self.item_mean_std.setItem(i, j, QTableWidgetItem(str(temp_data.values[i][j])))

	def hello(self):
		self.file_path.setText("hello world!")
		print("hello world")
		self.update_item_mean_std()

app = QtWidgets.QApplication(sys.argv)
#MainWindow = QMainWindow()
window = Ui_MainWindow()
window.show()

sys.exit(app.exec_())


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.setupUi(self)
	
	def update_item_mean_std(self, temp_data, column, row):
		head = ['Special Build Description', 'mean', 'median', 'std']
		self.item_mean_std.setColumnCount(column)
		self.item_mean_std.setRowCount(row)
		self.item_mean_std.setHorizontalHeaderLabels(head)
		for i in range(0, row):
			for j in range(0, column):
				self.item_mean_std.setItem(i, j, QTableWidgetItem(str(temp_data.values[i][j])))
	
	def hello(self):
		self.file_path.setText("hello world!")
		print("hello world")
		self.update_item_mean_std()


# app = QtWidgets.QApplication(sys.argv)
# # MainWindow = QMainWindow()
# window = mywindow()
# window.show()

# temp_data = pd.read_csv(r'C:\Users\TianJian\Desktop\python\UI\cpk.csv', header=0)
# print(temp_data)
# column = 4
# row = temp_data.count().values[0]
# print(row)
# mywindow.update_item_mean_std(temp_data,column, row)

# sys.exit(app.exec_())
