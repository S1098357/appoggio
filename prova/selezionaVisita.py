from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class selezionaVisita(QDialog):

    def __init__(self):
        super(selezionaVisita, self).__init__()
        loadUi('selezionaVisita.ui', self)

    def stampa(self,login):
        login.close()
        self.show()