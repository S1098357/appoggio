from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class AnnuncioGUI(QDialog):

    def __init__(self):
        super(AnnuncioGUI, self).__init__()
        loadUi("AnnuncioGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.textEdit.toPlainText()

    def indietro(self):
        self.close()
        return None