from vista.gestionar_vestudiante import *

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Gestionar_VEstudiante()
    w.show()
    sys.exit(app.exec_())