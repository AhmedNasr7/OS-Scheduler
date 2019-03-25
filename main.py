from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from Qtable import *


Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.window_width = 900
        self.window_height = 600
        self.setup_Ui()
        self.init_Buttons()

        self.processes_table = Table()


    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.center_window()
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(self.window_width,self.window_height)
        self.algorithmsMenu.addItem("  First Come First Serve")
        self.algorithmsMenu.addItem("  Shortest Job First")
        self.algorithmsMenu.addItem("  Priority")
        self.algorithmsMenu.addItem("  Round Robin")
        self.init_checkBoxes()
        self.algorithmsMenu.activated[str].connect(self.onActivation)
        




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


    def init_checkBoxes(self):

        self.preemptiveCheckBox = QCheckBox(' Preemptive ', self)
        self.nonPreemptiveCheckBox = QCheckBox(' Non Preemptive ', self)
      
        self.preemptiveCheckBox.move(310, 90)
        self.nonPreemptiveCheckBox.move(310, 120)
        self.preemptiveCheckBox.resize(350, 40)
        self.nonPreemptiveCheckBox.resize(350, 40)
        self.preemptiveCheckBox.stateChanged.connect(self.preemptive_stateChanged)
        self.nonPreemptiveCheckBox.stateChanged.connect(self.nonPreemptive_stateChanged)
        self.preemptiveCheckBox.setVisible(False)
        self.nonPreemptiveCheckBox.setVisible(False)

    def onActivation(self, algo):
        # on picking an algorithm from the menu

        try:

            if (algo == '  Priority'): #  showing preemptive/Non Preemptive checkboxes.
               self.preemptiveCheckBox.setVisible(True)
               self.nonPreemptiveCheckBox.setVisible(True)

            else:
                self.preemptiveCheckBox.setVisible(False)
                self.nonPreemptiveCheckBox.setVisible(False)

                
        except Exception as e:
            print(e)
                


    def add_processes(self):
        self.processes_table.show()


        
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










def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



