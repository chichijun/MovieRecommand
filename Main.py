# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from Gui import Ui_MainWindow

if(__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)

    createUi = Ui_MainWindow()
    Ui = QtGui.QMainWindow()
    createUi.setupUi(Ui)
    Ui.resize(1300, 800)
    Ui.move(300, 200)
    Ui.show()

    sys.exit(app.exec_())