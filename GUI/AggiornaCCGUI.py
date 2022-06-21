from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class AggiornaCCGUI(QDialog):

    def __init__(self,patologie):
        super(AggiornaCCGUI, self).__init__()
        loadUi("AggiornaCCGUI.ui", self)
        self.lineEdit.setPlainText(patologie)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.lineEdit.toPlainText()

    def indietro(self):
        self.close()
        return None