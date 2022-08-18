from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Grafico_Canvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(facecolor='0.94')
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)