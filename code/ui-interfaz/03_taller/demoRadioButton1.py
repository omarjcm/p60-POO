from demoRadioButton1_ui import *

class DemoRadioButton1(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.radioButtonFirstClass.toggled.connect( self.mostrar_mensaje )
        self.radioButtonBusinessClass.toggled.connect( self.mostrar_mensaje )
        self.radioButtonEconomyClass.toggled.connect( self.mostrar_mensaje )

    def mostrar_mensaje(self):
        self.valor = 0
        
        if self.radioButtonFirstClass.isChecked():
            self.valor = 150
        elif self.radioButtonBusinessClass.isChecked():
            self.valor = 125
        elif self.radioButtonEconomyClass.isChecked():
            self.valor = 100

        self.labelFare.setText( 'Value: ${}'.format(self.valor) )

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoRadioButton1()
    window.show()
    app.exec_()