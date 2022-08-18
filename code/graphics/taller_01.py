from graficos import *
from PyQt5.QtGui import QPainter

class Arturito(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def paintEvent(self, evet):
        self.paint = QPainter(self)
        self.paint.drawRect(100,15, 300, 10)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Arturito()
    app.exec_()    