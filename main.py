from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon
from processesTable import *
from chart import *
from scheduler import *

import numpy as np

#Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow):

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        #self.setupUi(self)
        self.window_width = 1100
        self.window_height = 1000
        self.setup_Ui()
        self.init_Buttons()
        self.proc_Gantt = []
        self.waiting_time = 0
        


        


    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.center_window()
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(self.window_width,self.window_height)
        self.algorithmsMenu = QComboBox(self)
        self.algorithmsMenu.move(30, 70)
        self.algorithmsMenu.resize(210, 40)
        self.algorithmsMenu.addItem("  First Come First Serve")
        self.algorithmsMenu.addItem("  Shortest Job First")
        self.algorithmsMenu.addItem("  Priority")
        self.algorithmsMenu.addItem("  Round Robin")
        self.add_processesBtn = QPushButton('Add Processes', self)
        self.add_processesBtn.move(640, 70)
        self.add_processesBtn.resize(130, 40)

        self.runBtn = QPushButton('Run Scheduler', self)
        self.runBtn.move(800, 70)
        self.runBtn.resize(130, 40)
        self.runBtn.setEnabled(0)

        self.waitingTimeLabel = QLabel('Waiting Time: ', self)
        self.waitingTimeLabel.move(450, 70)
        self.waitingTimeLabel.resize(150, 40)
        self.waitingTimeLabel.setVisible(0)

        self.algorithmsMenuLabel = QLabel('Choose Algorithm', self)
        self.algorithmsMenuLabel.move(30, 30)
        self.algorithmsMenuLabel.resize(200, 30)
        self.init_optionsWidgets()

        self.algorithmsMenu.activated[str].connect(self.algorithmMenu_onActivation)
        if (str(self.algorithmsMenu.currentText()) == '  Priority'):
            self.priorityPicked = True
        else:
            self.priorityPicked = False
        
        # GANTT Chart

        self.chart = PlotCanvas()
        self.layout().addWidget(self.chart)
        self.chart.move(20, 120)
        self.chart.resize(900, 600)
        self.chart.setVisible(0)

        p = [[3, 4], [0, 8], [1, 11], [2, 15], [3, 18], [0, 19], [2, 23], [2, 25]]

        #self.chart.plot(p)

    
        

    def center_window(self):
        # centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        


    def init_Buttons(self):
        '''
        Buttons initializations goes here
        '''
        self.add_processesBtn.clicked.connect(self.add_processes)
        self.runBtn.clicked.connect(self.run)



    def init_optionsWidgets(self):

        # Creating Preemption checkboxes:

        self.preemptiveCheckBox = QCheckBox(' Preemptive ', self)
        self.nonPreemptiveCheckBox = QCheckBox(' Non Preemptive ', self)
      
        self.preemptiveCheckBox.move(290, 55)
        self.nonPreemptiveCheckBox.move(290, 85)
        self.preemptiveCheckBox.resize(150, 40)
        self.nonPreemptiveCheckBox.resize(150, 40)
        self.preemptiveCheckBox.stateChanged.connect(self.preemptive_stateChanged)
        self.nonPreemptiveCheckBox.stateChanged.connect(self.nonPreemptive_stateChanged)
        self.preemptiveCheckBox.setVisible(False)
        self.nonPreemptiveCheckBox.setVisible(False)
        self.preemptiveCheckBox.setChecked(True)

        # creating Quantum Time Options
        self.QtimeLabel = QLabel('Enter Quantum Time', self)
        self.QtimeLabel.move(310, 30)
        self.QtimeLabel.resize(200, 40)
        self.QtimeEdit = QLineEdit(self)
        self.QtimeEdit.move(310, 70)
        self.QtimeEdit.resize(100, 40)
        self.QtimeEdit.setVisible(0)
        self.QtimeLabel.setVisible(0)
        



        
        

    def algorithmMenu_onActivation(self, algo):
        # on picking an algorithm from the menu

        try:

            if (algo == '  Priority'): #  showing preemptive/Non Preemptive checkboxes.
               self.preemptiveCheckBox.setVisible(True)
               self.nonPreemptiveCheckBox.setVisible(True)
               self.priorityPicked = True
               self.QtimeEdit.setVisible(0)
               self.QtimeLabel.setVisible(0)
            elif algo == "  Shortest Job First":
                
                self.preemptiveCheckBox.setVisible(True)
                self.nonPreemptiveCheckBox.setVisible(True)
                self.priorityPicked = False
                self.QtimeEdit.setVisible(0)
                self.QtimeLabel.setVisible(0)


            else:
                self.preemptiveCheckBox.setVisible(False)
                self.nonPreemptiveCheckBox.setVisible(False)
                self.priorityPicked = False
                if(algo == "  Round Robin"):
                    self.QtimeEdit.setVisible(1)
                    self.QtimeLabel.setVisible(1)
                else:
                    self.QtimeEdit.setVisible(0)
                    self.QtimeLabel.setVisible(0)


            

                
        except Exception as e:
            print(e)

        #self.add_processesBtn.clicked.connect(self.add_processes)
                


    def add_processes(self):

        self.processes_table = Table(self.priorityPicked)
        self.processes_table.show()
        self.processes_table.procAdded.connect(self.processAdded)
        self.chart.setVisible(0)



        
    def preemptive_stateChanged(self, state):
        
        if state == QtCore.Qt.Checked:
            self.nonPreemptiveCheckBox.setChecked(0)
            # do other stuff
        else:
            self.nonPreemptiveCheckBox.setChecked(1)
        
    
    def nonPreemptive_stateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.preemptiveCheckBox.setChecked(0)
            # do other stuff
        else:
            self.preemptiveCheckBox.setChecked(1)

    def processAdded(self):
        self.processes = self.processes_table.get_processes()
        print(self.processes)
        self.runBtn.setEnabled(1)
    
    def run(self):

        # run the corresponding algo
        if (str(self.algorithmsMenu.currentText()) == "  First Come First Serve"):
            self.proc_Gantt, self.waiting_time = FCFS(np.array(self.processes))
        
        elif (str(self.algorithmsMenu.currentText()) == '  Priority'):
            
            if self.preemptiveCheckBox.isChecked:
                self.proc_Gantt, self.waiting_time = Priority(np.array(self.processes), True)
            else:
                self.proc_Gantt, self.waiting_time = Priority(np.array(self.processes), False)

        
        elif (str(self.algorithmsMenu.currentText()) == "  Shortest Job First"):

            if self.preemptiveCheckBox.isChecked:
                self.proc_Gantt, self.waiting_time = SJF(np.array(self.processes), True)
            else:
                self.proc_Gantt, self.waiting_time = SJF(np.array(self.processes), False)
        
        elif (str(self.algorithmsMenu.currentText()) == "  Round Robin"):
            q = self.QtimeEdit.text()
            self.proc_Gantt, self.waiting_time = roundRobin(np.array(self.processes), int(q))
        
        else: 
            pass

        
        self.chart.plot(self.proc_Gantt)
        self.chart.setVisible(1)
        self.waitingTimeLabel.setVisible(1)
        self.waitingTimeLabel.setText("Average Waiting Time: " + str(self.waiting_time))

    

        

        
       
        






def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



