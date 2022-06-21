from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class StampaCertificatoGUI(QDialog):

    def __init__(self,certificato):
        super(StampaCertificatoGUI, self).__init__()
        loadUi("AnnuncioGUI.ui", self)
        self.label_3=certificato.nomePaziente
        self.label_7=certificato.nomeCognomeDottore
        self.label_8=certificato.DataRilascio
        if certificato.prezzo==50.00:
            self.label_9='agonistico'
        elif certificato.prezzo==100.00:
            self.label_9='sana e robusta costituzione'
        else:
            self.label_9='malattia'
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None
