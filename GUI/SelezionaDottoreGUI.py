from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SelezionaDottoreGUI(QDialog):

    def __init__(self,listaDottori):
        super(SelezionaDottoreGUI, self).__init__()
        loadUi("SelezionaDottoreGUI.ui", self)
        self.comboBox.addItems(listaDottori)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        match self.comboBox.currentText():
            case 'Simone Sgalla':
                return 0
            case 'Andrea Marini':
                return 1
            case 'Enrico Conradini':
                return 2
            case 'Domenico Ursino':
                return 3

    def indietro(self):
        self.close()
        return None
