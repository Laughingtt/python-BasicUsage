import sys
from PyQt5 import QtCore,QtGui,uic



qtCreatorFile = "untitled.ui" #Window File

Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class App(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnSub.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.textPrice.toPlainText())
        tax = float(self.dSBPer.value())
        total_price = price-((tax/100)*price)
        total_price_string = u"你要记得你要花多少钱，预计的价格很便宜啊："+str(total_price) +u"块"+"\n"+u"看到没有，还不快买"
        self.labelResult.setText(total_price_string )
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())