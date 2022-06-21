from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MenuSegreteriaGUI(QDialog):

    def __init__(self):
        super(MenuSegreteriaGUI, self).__init__()
        loadUi("MenuSegreteriaGUI.ui", self)
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.ret0)
        self.pushButton_2.clicked.connect(self.ret1)
        self.pushButton_3.clicked.connect(self.ret2)
        self.pushButton_4.clicked.connect(self.ret3)
        self.pushButton_8.clicked.connect(self.ret4)
        self.pushButton_5.clicked.connect(self.ret5)
        self.pushButton_7.clicked.connect(self.ret6)
        self.pushButton_6.clicked.connect(self.ret7)

    def ret0(self):
        self.close()
        return 0

    def ret1(self):
        self.close()
        return 1

    def ret2(self):
        self.close()
        return 2

    def ret3(self):
        self.close()
        return 3

    def ret4(self):
        self.close()
        return 4

    def ret5(self):
        self.close()
        return 5

    def ret6(self):
        self.close()
        return 6

    def ret7(self):
        self.close()
        return 7