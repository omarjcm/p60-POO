from select import select
from demoCheckBox1_ui import *

class DemoCheckBox(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.checkBoxCheese.stateChanged.connect( self.mostrar_monto )
        self.checkBoxOlives.stateChanged.connect( self.mostrar_monto )
        self.checkBoxSausages.stateChanged.connect( self.mostrar_monto )

    def mostrar_monto(self):
        self.monto = 10
        if self.checkBoxCheese.isChecked():
            self.monto += 1
        if self.checkBoxOlives.isChecked():
            self.monto += 1
        if self.checkBoxSausages.isChecked():
            self.monto += 2

        self.labelAmount.setText( 'El valor total de la pizza es ${}.'.format(self.monto) )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoCheckBox()
    window.show()
    app.exec_()