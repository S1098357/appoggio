from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class StampaDocumentiGUI(QDialog):

    def __init__(self):
        super(StampaDocumentiGUI, self).__init__()
        loadUi("StampaDocumentiGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.ricetta)
        self.pushButton_2.clicked.connect(self.ricevuta)
        self.pushButton_3.clicked.connect(self.certificato)
        self.pushButton_4.clicked.connect(self.indietro)

    def ricetta(self):
        self.close()
        return 0

    def ricevuta(self):
        self.close()
        return 2

    def certificato(self):
        self.close()
        return 1

    def indietro(self):
        self.close()
        return None
