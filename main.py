from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon


Ui_MainWindow,_ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setup_Ui()
        self.init_Buttons()

    def setup_Ui(self):
        '''
        UI setup goes here
        '''
        self.setWindowTitle("OS Scheduler")
        self.setFixedSize(900,600)

    def init_Buttons(self):
        '''
        Buttons initializations goes here
        '''
        pass

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



