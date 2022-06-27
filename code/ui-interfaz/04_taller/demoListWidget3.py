from demoListWidget3_ui import *

class DemoListWidget3(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButtonAdd.clicked.connect(self.agregar_valor)

    def agregar_valor(self):
        self.listWidgetSelectedItems.addItem( self.lineEditFoodItem.text() )
        self.lineEditFoodItem.setText('')
        self.lineEditFoodItem.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoListWidget3()
    window.show()
    app.exec_()
