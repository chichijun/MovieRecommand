# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import jieba
import re
from Huang import query
from MyBrowser import MyBrowser
from MyResultListWidget import MyResultListWidget
from Graphic1 import DrawWidget1
from Graphic2 import DrawWidget2
from Graphic3 import DrawWidget3
from Graphic4 import DrawWidget4
import codecs

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 624)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.queryLabel = QtGui.QLabel(self.centralwidget)
        self.queryLabel.setObjectName(_fromUtf8("queryLabel"))
        self.gridLayout.addWidget(self.queryLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.queryTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.queryTextEdit.setObjectName(_fromUtf8("queryTextEdit"))
        self.horizontalLayout_2.addWidget(self.queryTextEdit)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.submitBtn = QtGui.QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.verticalLayout_2.addWidget(self.submitBtn)
        self.clearBtn = QtGui.QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.verticalLayout_2.addWidget(self.clearBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.resultLabel = QtGui.QLabel(self.centralwidget)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.gridLayout.addWidget(self.resultLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.resultListWidget = MyResultListWidget(MainWindow)
        self.resultListWidget.setObjectName(_fromUtf8("resultListWidget"))
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.resultListWidget.addItem(item)
        self.verticalLayout.addWidget(self.resultListWidget)
        self.DetialTextBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.DetialTextBrowser.setObjectName(_fromUtf8("DetialTextBrowser"))
        self.verticalLayout.addWidget(self.DetialTextBrowser)
        self.browserBtn = QtGui.QPushButton(self.centralwidget)
        self.browserBtn.setObjectName(_fromUtf8("browserBtn"))
        self.verticalLayout.addWidget(self.browserBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.graphicTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.graphicTabWidget.setObjectName(_fromUtf8("graphicTabWidget"))
        self.tab1 = DrawWidget1()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.graphicTabWidget.addTab(self.tab1, _fromUtf8(""))
        # self.tab2 = DrawWidget2()
        # self.tab2.setObjectName(_fromUtf8("tab2"))
        # self.graphicTabWidget.addTab(self.tab2, _fromUtf8(""))
        # self.tab3 = QtGui.QWidget()
        # self.tab3.setObjectName(_fromUtf8("tab3"))
        # self.graphicTabWidget.addTab(self.tab3, _fromUtf8(""))
        # self.tab4 = QtGui.QWidget()
        # self.tab4.setObjectName(_fromUtf8("tab4"))
        # self.graphicTabWidget.addTab(self.tab4, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.graphicTabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 2, 1)
        self.detialLabel = QtGui.QLabel(self.centralwidget)
        self.detialLabel.setObjectName(_fromUtf8("detialLabel"))
        self.gridLayout.addWidget(self.detialLabel, 2, 0, 1, 1)
        self.queryLabel.raise_()
        self.submitBtn.raise_()
        self.clearBtn.raise_()
        self.queryTextEdit.raise_()
        self.resultLabel.raise_()
        self.resultListWidget.raise_()
        self.DetialTextBrowser.raise_()
        self.graphicTabWidget.raise_()
        self.graphicTabWidget.raise_()
        self.detialLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.graphicTabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.submitBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.onClickSubmitBtn)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.queryTextEdit.clear)
        QtCore.QObject.connect(self.resultListWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")),
                               self.onResultListWidgetItemClicked)
        QtCore.QObject.connect(self.browserBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.onClickOpenBrowserBtn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.queryLabel.setText(_translate("MainWindow", "请输入查询语句：", None))
        self.submitBtn.setText(_translate("MainWindow", "确定", None))
        self.clearBtn.setText(_translate("MainWindow", "清除", None))
        self.resultLabel.setText(_translate("MainWindow", "查询结果：", None))
        __sortingEnabled = self.resultListWidget.isSortingEnabled()
        self.resultListWidget.setSortingEnabled(False)
        item = self.resultListWidget.item(0)
        item.setText(_translate("MainWindow", "推荐电影No.1：", None))
        item = self.resultListWidget.item(1)
        item.setText(_translate("MainWindow", "推荐电影No.2：", None))
        item = self.resultListWidget.item(2)
        item.setText(_translate("MainWindow", "推荐电影No.3：", None))
        item = self.resultListWidget.item(3)
        item.setText(_translate("MainWindow", "推荐电影No.4：", None))
        item = self.resultListWidget.item(4)
        item.setText(_translate("MainWindow", "推荐电影No.5：", None))
        item = self.resultListWidget.item(5)
        item.setText(_translate("MainWindow", "推荐电影No.6：", None))
        item = self.resultListWidget.item(6)
        item.setText(_translate("MainWindow", "推荐电影No.7：", None))
        item = self.resultListWidget.item(7)
        item.setText(_translate("MainWindow", "推荐电影No.8：", None))
        item = self.resultListWidget.item(8)
        item.setText(_translate("MainWindow", "推荐电影No.9：", None))
        item = self.resultListWidget.item(9)
        item.setText(_translate("MainWindow", "推荐电影No.10：", None))
        self.resultListWidget.setSortingEnabled(__sortingEnabled)
        self.browserBtn.setText(_translate("MainWindow", "打开浏览器", None))
        self.graphicTabWidget.setTabText(self.graphicTabWidget.indexOf(self.tab1), _translate("MainWindow", "图1", None))
        self.detialLabel.setText(_translate("MainWindow", "详情信息：", None))

    def onClickSubmitBtn(self):
        if (self.queryTextEdit.toPlainText().isEmpty()):
            qtm = QtGui.QMessageBox(QtGui.QMessageBox.Warning, u'出错了',
                                    u'请在查询框中输入对电影的要求 。', QtGui.QMessageBox.Ok)
            qtm.exec_()
        else:
            queryString = str(self.queryTextEdit.toPlainText().toUtf8())
            seg_list = jieba.cut(queryString)
            querySegs = ''
            for seg in seg_list:
                querySegs += seg
                querySegs += ' '

            querySegs = re.sub('[~·！@#￥%……&*（）——-]'.decode('UTF-8'), ' '.decode('UTF-8'), querySegs)
            querySegs = re.sub('[+={【}】|、：；“‘”’《，》。？/]'.decode('UTF-8'), ' '.decode('UTF-8'), querySegs)
            querySegs = re.sub(' +'.decode('UTF-8'), ' '.decode('UTF-8'), querySegs)

            results = []
            rank = []
            mapping=[]
            rank,results,mapping = query(querySegs)
            movieList = []
            for i in range(10):
                movieList.append(mapping[results[i]])

            self.resultListWidget.clearResultList()
            self.resultListWidget.setResultList(movieList)

            for i in range(0, 10):
                self.resultListWidget.item(i).setText(_translate("MainWindow",
                                                      self.resultListWidget.resultList[i], None))

            self.tab1.draw_pic(rank,results)

            for i in range(0,10):
                print self.resultListWidget.resultList[i]
                print self.resultListWidget.resultDetialList[i]

    def onResultListWidgetItemClicked(self):
        index = 0
        curItemContent = self.resultListWidget.currentItem().text()
        for i in range(0, 10):
            if(curItemContent == self.resultListWidget.item(i).text()):
                index = i
                break
            ++index

        detial = self.resultListWidget.resultDetialList[index]
        #Python2默认是ASCII编码。虽然通过魔法注释可以解决源文件的编码问题。
        #但是，如果涉及到‘’+ u‘’的操作的时候，ASCII和unicode的编码格式还是不一样。
        #所以这里直接就是detial了。
        self.DetialTextBrowser.setText(_translate("MainWindow", detial, None))

    def onClickOpenBrowserBtn(self):
        self.browser = MyBrowser()
        self.browser.show()





