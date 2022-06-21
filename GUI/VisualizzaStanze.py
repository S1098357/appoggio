from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaStanze(QDialog):

    def __init__(self, StanzeOccupate, StanzeLibere):
        super(VisualizzaStanze, self).__init__()
        loadUi("Visualizza Stanze.ui", self)
        for i in range (1,3):
            if StanzeOccupate[i] == True:
                self.comboBox_2 = StanzeOccupate[i].numeroDiStanza
            elif StanzeLibere[i]==True:
                self.comboBox = StanzeLibere[i].numeroDiStanza
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None