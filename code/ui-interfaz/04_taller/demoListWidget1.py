from demoListWidget1_ui import *

class DemoListWidget1(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        item = QtWidgets.QListWidgetItem()
        item.setText('Otro valor.')
        self.listWidgetDiagnosis.addItem(item)

        self.listWidgetDiagnosis.itemClicked.connect(self.mostrar_seleccionado)

    def mostrar_seleccionado(self):
        self.labelTest.setText( 'Has seleccionado {}.'.format(self.listWidgetDiagnosis.currentItem().text()) )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoListWidget1()
    window.show()
    app.exec_()
