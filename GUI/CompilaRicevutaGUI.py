from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class CompilaRicevutaGUI(QDialog):

    def __init__(self):
        super(CompilaRicevutaGUI, self).__init__()
        loadUi('CompilaRicevutaGUI.ui',self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.si )
        self.pushButton_2.clicked.connect(self.no)

    def si(self):
        self.close()
        return True

    def no(self):
        self.close()
        return False
