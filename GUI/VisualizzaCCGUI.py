from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class VisualizzaCCGUI(QDialog):

    def __init__(self,patologie):
        super(VisualizzaCCGUI, self).__init__()
        loadUi("VisualizzaCCGUI.ui", self)
        self.textBrowser=patologie
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.indietro)

    def indietro(self):
        self.close()
        return None
