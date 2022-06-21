from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SelezionaGiornoGUI(QDialog):

    def __init__(self):
        super(SelezionaGiornoGUI, self).__init__()
        loadUi("SelezionaGiornoGUI.ui", self)
        self.comboBox.addItems('lunedì','martedì','mercoledì','giovedì','venerdì')
        self.comboBox.addItems('10.00-16.00', '11.00-17.00', '12.00-18.00')
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        match self.comboBox.currentText():
            case 'lunedì':
                appoggio= 0
            case 'martedì':
                appoggio= 1
            case 'mercoledì':
                appoggio= 2
            case 'giovedì':
                appoggio= 3
            case 'venerdì':
                appoggio= 4
        match self.comboBox.currentText():
            case '10.00-16.00':
                orario= datetime.time(hours=10.00)
            case '11.00-17.00':
                orario= datetime.time(hours=11.00)
            case '12.00-18.00':
                orario= datetime.time(hours=12.00)
        return (appoggio,orario)

    def indietro(self):
        self.close()
        return None