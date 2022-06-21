from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.ModificaPrenotazioneGUI import ModificaPrenotazioneGUI


class VisualizzaPrenotazioneGUI(QDialog):

    def __init__(self,prenotazione):
        super(VisualizzaPrenotazioneGUI, self).__init__()
        loadUi("Visualizza Dopo.ui", self)
        self.label_3 = prenotazione.cliente
        self.label_5 = prenotazione.dottore
        self.label_9 = prenotazione.dataOra
        self.label_10 = prenotazione.tipoAppuntamento
        self.textEdit = prenotazione.note
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None