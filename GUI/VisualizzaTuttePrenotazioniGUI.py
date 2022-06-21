from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaTuttePrenotazioniGUI(QDialog):

    def __init__(self, listaPrenotazioni):
        super(VisualizzaTuttePrenotazioniGUI, self).__init__()
        loadUi("VisualizzaTuttePrenotazioniGUI.ui", self)
        for prenotazione in listaPrenotazioni:
            lista = prenotazione.dataOra + '\n'
        self.textBrowser = lista
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None