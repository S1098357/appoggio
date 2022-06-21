from PyQt5 import *
from PyQt5.QtWidgets import*
from PyQt5.uic import *
import sys
from prova.selezionaVisita import selezionaVisita
from prova.menuCliente import menuCliente

class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi('Login.ui',self)

    def loginFunction(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        self.show()
        #self.pushButton.clicked.connect(lambda :self.prova.stampa())
        return username,password

app=QApplication(sys.argv)
form = menuCliente()
form.prova()
pag2 = selezionaVisita()
form.pushButton.clicked.connect(lambda: pag2.stampa(form))
sys.exit(app.exec_())