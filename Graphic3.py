#_*_coding:utf-8_*_

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys


class DrawWidget3(QWidget):
    def __init__(self, parent=None):
        super(DrawWidget3, self).__init__(parent)
        figure = plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
        canvas = figureCanvas(figure)

        plt.axes([0.1, 0.1, 0.5, 0.5])
        plt.xticks([])
        plt.yticks([])
        plt.text(0.2, 0.2, 'hello axes', alpha='0.65', size=16)

        plt.text(0.6, 0.4, 'hello axes', alpha='0.65', size=16)

        canvas.draw()
        layout = QHBoxLayout(self)
        layout.addWidget(canvas)