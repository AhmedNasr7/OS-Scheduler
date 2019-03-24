from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "Processes.ui"))

class Table(QMainWindow, Ui_MainWindow):

    def __init__(self, parent= None):
        super(Table, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setup_Ui()
        self.init_Button()


    def setup_Ui(self):
        '''
        UI setup goes here
        '''

        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(800,600)
        self.table.move(0, 0)
        self.table.setFixedSize(600, 400)
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        self.enterButton = QPushButton('Enter Processes', self)
        self.enterButton.resize(150, 40)
        self.enterButton.move(620, 50)
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.resize(150, 40)
        self.cancelButton.move(620, 100)

        #self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.table.resizeColumnsToContents



    def init_Button(self):
        self.enterButton.clicked.connect(self.onClick_enterButton)
        self.cancelButton.clicked.connect(self.onClick_cancelButton)




    def onClick_enterButton(self):
        print("enter clicked")

    
    def onClick_cancelButton(self):
        print('cancel Clicked')




    
    '''
    def accept(self):
        print("Hello")
    
    def reject(self):
        print("World")
    '''
        
        
            

def main():
    app = QApplication(sys.argv)
    window = Table()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



