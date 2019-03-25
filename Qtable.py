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
        self.columns_count = 3
        self.rows_count = 5
        self.table_width = 600
        self.table_height = self.rows_count * 34
        self.setup_Ui()
        self.init_Button()
    
       



    def setup_Ui(self):
        '''
        UI setup goes here
        '''

        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(800,600)
        self.table.move(0, 0)
        self.table.setFixedSize(self.table_width, self.table_height)
        self.table.setRowCount(self.rows_count)
        self.table.setColumnCount(self.columns_count)
        for i in range(self.columns_count):
             self.table.setColumnWidth(i, self.table_width/3 - 10)
        
        self.enterButton = QPushButton('Enter Processes', self)
        self.enterButton.resize(150, 40)
        self.enterButton.move(620, 50)
        self.add_newRow = QPushButton("Add New Row", self)
        self.add_newRow.resize(150, 40)
        self.add_newRow.move(620, 100)
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.resize(150, 40)
        self.cancelButton.move(620, 150)
        

        #self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.table.resizeColumnsToContents



    def init_Button(self):
        self.enterButton.clicked.connect(self.onClick_enterButton)
        self.add_newRow.clicked.connect(self.addRow)
        self.cancelButton.clicked.connect(self.onClick_cancelButton)



    def onClick_enterButton(self):
        pass

    def addRow(self):
        self.rows_count += 1
        if self.table_height < 34 * self.rows_count:
            self.table_height += 34
            
        self.table.setFixedSize(self.table_width, self.table_height)
        self.table.setRowCount(self.rows_count)

    
    def onClick_cancelButton(self):
        pass




    
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



