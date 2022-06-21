from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SceltaPrenotazioneGUI(QDialog):

    def __init__(self):
        super(SceltaPrenotazioneGUI, self).__init__()
        loadUi("SceltaPrenotazioneGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton_3.clicked.connect(self.visualizzaTutte)
        self.pushButton_2.clicked.connect(self.visualizzaPerDottore)
        self.pushButton_4.clicked.connect(self.indietro)

    def visualizzaTutte(self):
        self.close()
        return False

    def visualizzaPerDottore(self):
        self.close()
        return True

    def indietro(self):
        self.close()
        return None