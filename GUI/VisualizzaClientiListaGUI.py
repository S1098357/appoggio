from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class VisualizzaClientiListaGUI(QDialog):

    def __init__(self, listaClienti):
        super(VisualizzaClientiListaGUI, self).__init__()
        loadUi("Visualizza Tutti i Clienti.ui", self)
        for cliente in listaClienti:
            lista = cliente.nome + '\n'
        self.textBrowser = lista
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None