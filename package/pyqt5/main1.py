import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from functools import partial  #传参
import test

def click_success(ui):
    print("啊哈哈哈我终于成功了！")
    txt=ui.lineEdit.text()  #获得input框的值
    ui.label.setText(txt)  #设定label的值

def read_file(ui):
    # 选取文件
    filename, filetype = QFileDialog.getOpenFileName(None, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
    print(filename, filetype)
    ui.lineEdit.setText(filename)

def write_folder(ui):
    # 选取文件夹
    foldername = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
    print(foldername)
    ui.lineEdit.setText(foldername)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(write_folder, ui))  #设置触发按钮的槽
    sys.exit(app.exec_())
