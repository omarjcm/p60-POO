from demoComboBox_ui import *

class DemoComboBox(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.comboBoxAccountType.addItem("Otro valor")

        self.comboBoxAccountType.currentIndexChanged.connect( self.seleccionar_elemento )

    def seleccionar_elemento(self):
        self.labelAccountType.setText( 'Has seleccionado {}.'.format(self.comboBoxAccountType.itemText( self.comboBoxAccountType.currentIndex() )) )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoComboBox()
    window.show()
    app.exec_()
