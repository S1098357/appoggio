from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class RUDClienteGUI(QDialog):

    def __init__(self):
        super(RUDClienteGUI, self).__init__()
        loadUi("RUDClienteGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.visualizza)
        self.pushButton_2.clicked.connect(self.modifica)
        self.pushButton_3.clicked.connect(self.elimina)
        self.pushButton_4.clicked.connect(self.indietro)

    def visualizza(self):
        self.close()
        return 0

    def modifica(self):
        self.close()
        return 1

    def elimina(self):
        self.close()
        return 2

    def indietro(self):
        self.close()
        return None