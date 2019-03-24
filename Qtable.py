from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Processes import Ui_Processes

Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "Processes.ui"))

class Table(QMainWindow, Ui_MainWindow):

    def __init__(self, parent= None):
        super(Table, self).__init__(parent)
        QMainWindow.__init__(self)
        # self.ui = Ui_Processes()
        self.setupUi(self)

    def accept(self):
        print("Hello")
    
    def reject(self):
        print("World")
        
        
            

def main():
    app = QApplication(sys.argv)
    window = Table()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



