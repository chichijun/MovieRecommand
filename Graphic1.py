#_*_coding:utf-8_*_

from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
from pylab import *

class DrawWidget1(QWidget):
    canvas = None
    layout = None

    def __init__(self,parent=None):
        super(DrawWidget1,self).__init__(parent)

        self.layout = QHBoxLayout(self)

    def draw_pic(self,radii,result):

        if(self.canvas is not None):
            self.layout.removeWidget(self.canvas)

        figure = plt.gcf() #返回当前的figure
        self.canvas = figureCanvas(figure)

        radii= [abs(1.0/i*20) for i in list(radii)]    
        ax = axes([0.025, 0.025, 0.95, 0.95], polar=True)  #axes(轴)代表维度,polar用来画极坐标图
        N = 10                                             #元素的个数
        theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)  # 是一个pi/10的递增的列表#print "theta=%s"%theta    
        width = np.pi/4*np.random.rand(N)  #小于4分之1 PI的随机数
        bars = plt.bar(theta, radii, width=width, bottom=0.0)
        i=0
        for r,bar in zip(radii, bars):  
            bar.set_facecolor( cm.jet(r/1000.))  
            bar.set_alpha(0.5)         
            height = bar.get_height()
            ax.text(bar.get_x()+bar.get_width()/2. , 1.03*height, "%s" % result[i])
            i+=1
        ax.set_xticklabels(["Funcitons"])  
        ax.set_yticklabels(["possiblitly"])   # savefig('figure/polar_ex_LSI.png', dpi=48)

        self.canvas.draw()
        self.layout.addWidget(self.canvas)


