from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MessaggioGUI(QDialog):

    def __init__(self,listaClienti):
        super(MessaggioGUI, self).__init__()
        loadUi("MessaggioGUI.ui", self)
        self.comboBox.addItems(listaClienti)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        return self.textEdit.toPlainText(),self.comboBox.currentText()

    def indietro(self):
        self.close()
        return None,None