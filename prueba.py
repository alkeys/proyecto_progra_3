#Ignora este archivo, solo es la prueba de GT
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class prueba_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.ui", self)
        self.boton1.clicked.connect(self.primerg)
        self.boton2.clicked.connect(self.segundog)
        self.boton3.clicked.connect(self.libreg)

    def primerg(self):
        self.info.setText("Ingrese los datos de\nla ecuación y = ax + c\n")

    def segundog(self):
        self.info.setText("Ingrese los datos de la ecuación aX\u00B2+bX+c\n")

    def libreg(self):
        pass

if __name__=='__main__':
    app = QApplication(sys.argv)
    GUI = prueba_GUI()
    GUI.show()
    sys.exit(app.exec_())
