# _*_coding:utf-8_*_

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys


class DrawWidget2(QWidget):
    def __init__(self, parent=None):
        super(DrawWidget2, self).__init__(parent)
        figure = plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
        canvas = figureCanvas(figure)
        x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        c = np.cos(x)
        s = np.sin(x)
        plt.plot(x, c, color='blue', linewidth=1.0, linestyle='-', label='$cos(x)$')  # 设置颜色，线条的格式和粗细
        plt.plot(x, s, color='green', linewidth=1.0, linestyle='-', label='$sin(x)$')

        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        plt.xlim(x.min() * 1.1, x.max() * 1.1)  # X轴的范围
        plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
                   [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])  # X轴的刻度值
        plt.ylim(s.min() * 1.1, s.max() * 1.1)  # Y轴的范围
        plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])  # 设置Y轴的刻度值,第二个参数对其进行格式化

        # 添加注释和箭头以及虚线
        t = np.pi * 2 / 3
        plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
        plt.scatter([t], [np.sin(t)], 50, color='red')  # 50代表散点的大小，应该是像素值

        plt.plot([t, t], [0, np.cos(t)], color='green', linewidth=2.5, linestyle='--')
        plt.scatter([t], [np.cos(t)], 50, color='green')

        plt.annotate(r'$sin(\frac{2\pi}{3})=(\frac{\sqrt{3}}{2})$',
                     xy=(t, np.sin(t)), xycoords='data',
                     xytext=(10, 30), textcoords='offset points', fontsize=16,
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.1'))
        plt.annotate(r'$cos(\frac{2\pi}{3})=(\frac{\sqrt{3}}{2})$',
                     xy=(t, np.cos(t)), xycoords='data',
                     xytext=(-120, -30), textcoords='offset points', fontsize=16,
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.1'))  # 后面的参数应该是角度，类似于偏离度，1的时候接近垂直
        plt.legend(loc='upper left')

        for i in ax.get_xticklabels() + ax.get_yticklabels():
            i.set_fontsize(15)
            i.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.65))

        canvas.draw()
        layout = QHBoxLayout(self)
        layout.addWidget(canvas)