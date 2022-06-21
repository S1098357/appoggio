from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI import VisualizzaTuttiClientiGUI


class SceltaVisualizzaClienteGUI(QDialog):

    def __init__(self):
        super(SceltaVisualizzaClienti, self).__init__()
        loadUi("Scelta Visualizza Clienti.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.visualizzaTuttiClienti)
        self.pushButton_2.clicked.connect(self.selezionaDottore)

    def visualizzaTuttiClienti(self):
        self.close()
        return False

    def selezionaDottore(self):
        self.close()
        return True