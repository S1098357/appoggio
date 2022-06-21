from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaDottoreGUI(QDialog):

    def __init__(self,dottore):
        super(VisualizzaDottoreGUI, self).__init__()
        loadUi("VisualizzaDottoreGUI", self)
        self.label_4=dottore.nomeCognome
        self.label_5=dottore.numeroDiTelefono
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None

