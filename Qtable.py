from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Processes import Ui_Processes



class Table(QMainWindow):

    def __init__(self, parent= None):
        super(Table, self).__init__(parent)
        QMainWindow.__init__(self)
        self.ui = Ui_Processes()
        self.ui.setupUi(self)
        self.setup_Ui()

    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(900,600)

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



