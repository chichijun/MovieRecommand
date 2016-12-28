from PyQt4 import QtGui

class MyResultListWidget(QtGui.QListWidget):
    resultList = []
    resultDetialList = []

    def __init__(self, parent = None):
        super(MyResultListWidget, self).__init__(parent)

    def setResultList(self, movieList):
        for movie in movieList:
            movie = movie.strip('\n')
            temp = (movie.split(' '))[0]
            self.resultList.append(temp)
            self.resultDetialList.append(movie)

    def clearResultList(self):
        self.resultList = []
        self.resultDetialList = []


