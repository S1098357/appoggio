from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class RUDPrenotazioneGUI(QDialog):

    def __init__(self):
        super(RUDPrenotazioneGUI, self).__init__()
        loadUi("RUDPrenotazioneGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton_3.clicked.connect(self.visualizza)
        self.pushButton_2.clicked.connect(self.elimina)
        self.pushButton_4.clicked.connect(self.indietro)

    def visualizza(self):
        self.close()
        return True

    def elimina(self):
        self.close()
        return False

    def indietro(self):
        self.close()
        return None