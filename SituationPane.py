import numpy as np
from PyQt5.Qt import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from UI.situation import Ui_Form


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)


class Situation(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def PrepareOne(self, ls1, ls2):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox_2)
        self.LineFigureLayout.addWidget(self.LineFigure)

        self.lines = self.LineFigure.ax.plot(np.array(ls1), np.array(ls2))

    def PrepareTwo(self, ls1, ls2):
        self.BarFigure = Figure_Canvas()
        self.BarFigureLayout = QGridLayout(self.groupBox)
        self.BarFigureLayout.addWidget(self.BarFigure)

        self.bar = self.BarFigure.ax.bar(np.array(ls1), np.array(ls2), width=0.4)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Situation()
    window.show()
    sys.exit(app.exec_())
