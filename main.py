#!/usr/bin/env python3

import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget

import matplotlib as mpl
mpl.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys
import math

class MyCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = mpl.figure.Figure()
        self.axes = fig.add_subplot(111)
        self.t = np.zeros(100)
        self.y = np.zeros(100)
        self.li, = self.axes.plot(self.t, self.y)
        self.axes.set_ylim(-1, 1)

        super(MyCanvas, self).__init__(fig)
        self.setParent(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update_fig)
        self.time = 0
        timer.start(100)

    def update_fig(self):
        self.time += math.pi/100
        self.t = np.append(self.t, self.time)
        self.t = np.delete(self.t, 0)
        self.y = np.append(self.y, math.sin(self.time))
        self.y = np.delete(self.y, 0)

        self.li.set_xdata(self.t)
        self.li.set_ydata(self.y)

        self.axes.set_xlim(min(self.t), max(self.t))

        self.draw()


def main():
    app = QApplication(sys.argv)

    c = MyCanvas()
    c.show()

    exit(app.exec())

if __name__ == '__main__':
    main()
