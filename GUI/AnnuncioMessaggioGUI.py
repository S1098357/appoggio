from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class AnnuncioMessaggioGUI(QDialog):

    def __init__(self):
        super(AnnuncioMessaggioGUI, self).__init__()
        loadUi("AnnuncioMessaggioGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton_2.clicked.connect(self.annuncio)
        self.pushButton.clicked.connect(self.messaggio)
        self.pushButton_3.clicked.connect(self.indietro)

    def annuncio(self):
        self.close()
        return True

    def messaggio(self):
        self.close()
        return False

    def indietro(self):
        self.close()
        return None