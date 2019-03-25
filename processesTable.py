from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox, QGridLayout, QDesktopWidget, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "Processes.ui"))

class Table(QMainWindow):

    def __init__(self, priority, parent= None):
        super(Table, self).__init__(parent)
        QMainWindow.__init__(self)
        #self.setupUi(self)
        self.columns_count = 3
        self.rows_count = 5
        self.table_width = 600
        self.table_height = self.rows_count * 34
        self.setup_Ui(priority)
        self.init_Button()
    
       



    def setup_Ui(self, priority):
        '''
        UI setup goes here
        '''
        self.center_window()
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(800,600)
        self.create_table(priority)
        self.runButton = QPushButton('Run Scheduler', self)
        self.runButton.resize(150, 40)
        self.runButton.move(620, 50)
        self.add_newRow = QPushButton("Add New Row", self)
        self.add_newRow.resize(150, 40)
        self.add_newRow.move(620, 100)
        self.deleteRowBtn = QPushButton('Delete Row', self)
        self.deleteRowBtn.resize(150, 40)
        self.deleteRowBtn.move(620, 150)
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.resize(150, 40)
        self.cancelButton.move(620, 200)
        
        

        #self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.table.resizeColumnsToContents

    def create_table(self, priority):
        if(priority): 
            self.columns_count = 4
            columnsLabels = ['Process Name', 'Burst Time', 'Arrival Time', 'Priority']
        else:
            columnsLabels = columnsLabels = ['Process Name', 'Burst Time', 'Arrival Time']

        self.table = QTableWidget()
        self.layout().addWidget(self.table)
        self.table.move(0, 0)
        self.table.setFixedSize(self.table_width, self.table_height)
        self.table.setRowCount(self.rows_count)
        self.table.setColumnCount(self.columns_count)
        for i in range(self.columns_count):
            self.table.setColumnWidth(i, self.table_width/self.columns_count - 10)
    
        self.table.setHorizontalHeaderLabels(columnsLabels)

    

    def init_Button(self):
        self.runButton.clicked.connect(self.onClick_runButton)
        self.add_newRow.clicked.connect(self.add_row)
        self.cancelButton.clicked.connect(self.onClick_cancelButton)
        self.deleteRowBtn.clicked.connect(self.delete_row)


    def center_window(self):
         # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


    def onClick_runButton(self):
        pass


    def add_row(self):
        self.rows_count += 1
        if self.table_height < 34 * self.rows_count:
            self.table_height += 34
            
        self.table.setFixedSize(self.table_width, self.table_height)
        self.table.setRowCount(self.rows_count)

    def delete_row(self):
        self.rows_count -= 1
        self.table_height -= 32
        self.table.setRowCount(self.rows_count)
        self.table.setFixedSize(self.table_width, self.table_height)

    
    def onClick_cancelButton(self):

         self.close()




  