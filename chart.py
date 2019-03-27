import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.pNames = []
        self.start = []
        self.end = []

       


    def plot(self, p):

        self.processData(p)

        self.ax.set_yticks(self.pNums)

        # Set ticks labels for x-axis
        self.ax.set_yticklabels(self.y_ticks_labels, rotation='horizontal', fontsize=9)
        self.ax.hlines(self.pNums, self.start, self.end, colors="blue", lw=10)
        self.ax.margins(0.1)
        self.ax.set_xticks(range(self.end[len(self.end) - 1] + 2))
        self.ax.set_xticklabels(range(self.end[len(self.end) - 1] + 2), rotation='vertical', fontsize=9)
        plt.show(self.ax)
            




    def processData(self, processes):

        self.y_ticks_labels = []
        self.pNums = []
        self.start = [0]
        
        for l in processes:
            self.y_ticks_labels.append('Process ' + str(l[0]))
            self.pNums.append(l[0])
            self.start.append(l[1])
            self.end.append(l[1])
        
        self.start.pop()

     

        

       
