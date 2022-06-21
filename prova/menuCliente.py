
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import *

from prova.selezionaVisita import selezionaVisita



class menuCliente(QDialog):

    def __init__(self):
        super (menuCliente,self).__init__()
        loadUi("MenuCLiente.ui",self)
        self.x=selezionaVisita()


    def prova(self):
        self.show()
        self.pushButton.clicked.connect(lambda:self.NuovaPrenotazione)

    def NuovaPrenotazione(self):
        self.x.show()