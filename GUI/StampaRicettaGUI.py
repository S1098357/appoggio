from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class StampaRicettaGUI(QDialog):

    def __init__(self, ricetta):
        super(StampaRicettaGUI, self).__init__()
        loadUi("StampaRicettaGui.ui", self)
        self.label_5 = ricetta.nomePaziente
        self.label_6 = ricetta.nomeCognomeDottore
        self.label_7 = ricetta.dataRilascio
        self.label_8 = ricetta.farmacoPrescritto
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None