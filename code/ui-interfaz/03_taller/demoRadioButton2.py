from demoRadioButton2_ui import *

class DemoRadioButton2(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.radioButtonLarge.toggled.connect(self.seleccionar)
        self.radioButtonMedium.toggled.connect(self.seleccionar)
        self.radioButtonXL.toggled.connect(self.seleccionar)
        self.radioButtonXXL.toggled.connect(self.seleccionar)

        self.radioButtonDebitCard.toggled.connect(self.seleccionar)
        self.radioButtonCashOnDelivery.toggled.connect(self.seleccionar)
        self.radioButtonNetBanking.toggled.connect(self.seleccionar)

    def seleccionar(self):
        self.seleccionado_1 = ''
        self.seleccionado_2 = ''

        if self.radioButtonLarge.isChecked():
            self.seleccionado_1 = 'Large'
        elif self.radioButtonMedium.isChecked():
            self.seleccionado_1 = 'Medium'
        elif self.radioButtonXL.isChecked():
            self.seleccionado_1 = 'XL'
        elif self.radioButtonXXL.isChecked():
            self.seleccionado_1 = 'XXL'
        
        if self.radioButtonCashOnDelivery.isChecked():
            self.seleccionado_2 = 'Cash on Delivery'
        elif self.radioButtonDebitCard.isChecked():
            self.seleccionado_2 = 'Debit Card'
        elif self.radioButtonNetBanking.isChecked():
            self.seleccionado_2 = 'Net Banking'

        self.labelSelected.setText( 'El tamanio de la camisa es: {} y el metodo del pago es {}.'.format(self.seleccionado_1, self.seleccionado_2) )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoRadioButton2()
    window.show()
    app.exec_()