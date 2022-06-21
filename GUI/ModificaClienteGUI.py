from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class ModificaClienteGUI(QDialog):

    def __init__(self):
        super(ModificaClienteGUI, self).__init__()
        loadUi("ModificaClienteGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()

    def indietro(self):
        self.close()
        return None,None,None