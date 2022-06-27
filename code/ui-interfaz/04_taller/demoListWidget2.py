from demoListWidget2_ui import *

class DemoListWidget2(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.listWidgetDiagnosis.itemSelectionChanged.connect(self.mostrar_seleccionados)

    def mostrar_seleccionados(self):
        self.listWidgetSelectedTests.clear()
        items = self.listWidgetDiagnosis.selectedItems()
        for i in list(items):
            self.listWidgetSelectedTests.addItem( i.text() )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoListWidget2()
    window.show()
    app.exec_()
