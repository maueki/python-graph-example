#!/usr/bin/env python3

import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget

import matplotlib as mpl
mpl.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys

class MyCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = mpl.figure.Figure()
        self.axes = fig.add_subplot(111)
        super(MyCanvas, self).__init__(fig)
        self.setParent(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update_fig)

        timer.start(100)

    def update_fig(self):
        print("call update")

def main():
    app = QApplication(sys.argv)

    c = MyCanvas()
    c.show()

    exit(app.exec())

if __name__ == '__main__':
    main()
