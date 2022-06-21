from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class EliminaCCGUI(QDialog):

    def __init__(self,listaCartelle):
        super(EliminaCCGUI, self).__init__()
        loadUi("EliminaCCGUI.ui", self)
        self.comboBox.addItems(listaCartelle.Id)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.comboBox.currentText()

    def indietro(self):
        self.close()
        return None
