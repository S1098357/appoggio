from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class LeggiRicevutaGUI(QDialog):

    def __init__(self,prezzo,data):
        super(LeggiRicevutaGUI, self).__init__()
        loadUi("LeggiRicevutaGUI.ui", self)
        self.label_2=prezzo
        self.label_4=data
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None