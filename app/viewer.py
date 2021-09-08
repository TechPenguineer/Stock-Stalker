
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *

TITLE = "Stock Stalker - Watcher - By TechPenguineer"
window = pg.plot()
window.setWindowTitle(TITLE)

Y=[6,3,5,1,-2,-5,3]
X=[1,2,3,4,5,6,7]

window.showGrid(y=True)
window.addLegend()
GRAPH = window.plot(X, Y, fillLevel=2, pen ='g', width=2, symbolPen ='g', name ='Price')
window.addItem(GRAPH)



if __name__ == '__main__':
    pg.exec()
