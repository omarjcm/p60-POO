from demoListWidgetOp_ui import *

class DemoListWidgetOp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        list = ['Helado', 'Coca Cola', 'Cafe', 'Chocolate']
        for elemento in list:
            self.listWidget.addItem(elemento)
        
        self.pushButtonAdd.clicked.connect( self.agregar_elemento )
        self.pushButtonEdit.clicked.connect( self.editar_elemento )
        self.pushButtonDelete.clicked.connect( self.eliminar_elemento )
        self.pushButtonDeleteAll.clicked.connect( self.eliminar_elementos )

    def agregar_elemento(self):
        self.listWidget.addItem( self.lineEdit.text() )
        self.lineEdit.setText('')
        self.lineEdit.setFocus()

    def editar_elemento(self):
        self.elemento = self.listWidget.currentRow()
        (nuevo_valor, ok) = QInputDialog.getText(self, 'Ingresar nuevo texto: ', 'Ingresar nuevo texto')
        if ok and len(nuevo_valor) != 0:
            self.listWidget.takeItem( self.listWidget.currentRow() )
            self.listWidget.insertRow(self.elemento, QListWidgetItem(nuevo_valor))

    def eliminar_elemento(self):
        pass

    def eliminar_elementos(self):
        pass

    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DemoListWidgetOp()
    window.show()
    app.exec_()
