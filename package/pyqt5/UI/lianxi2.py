from lianxi1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

#from mylog import LogAssistant


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.query_formula)
        # 给button 的 点击动作绑定一个事件处理函数


    #def query_formula(self):
        # 此处编写具体的业务逻辑




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())