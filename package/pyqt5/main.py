from PyQt5 import QtWidgets
from test import Ui_MainWindow  # 导入ui文件转换后的py文件
from PyQt5.QtWidgets import QFileDialog


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.write_folder)
        # self.pushButton2.clicked.connect(self.read_file)
        # self.pushButton3.clicked.connect(self.process)

    def read_file(self):
        # 选取文件
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        print(filename, filetype)
        self.lineEdit.setText(filename)

    def write_folder(self):
        # 选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        print(foldername)
        self.lineEdit.setText(foldername)

    # 进行处理
    def process(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
