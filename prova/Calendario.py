from datetime import datetime

from prova.Dottore import Dottore


class Calendario:

    def __init__(self):
        self.dataOdierna=datetime.date.today()
        self.Dottori=[Dottore('Enrico Corradini','3333333333'),Dottore('Andrea Marini','22222222222'),Dottore('Simone Sgalla','1111111111'),Dottore('Domenico Ursino','0000000000')]
        self.orarioStanzaVuota=[]
        self.stanzeOccupate=[False,False,False,False]

    def getListaDottori(self):
        return self.Dottori

    def aggiornaStanze(self):
        i=0
        for dottore in self.Dottori:
            if datetime.now>dottore.OrarioLavoro[datetime.weekday()] and datetime.now<dottore.OrarioLavoro[datetime.weekday()]+datetime.time(6):
                self.stanzeOccupate[i]=True
                self.orarioStanzaVuota[i]=dottore.OrarioLavoro[datetime.weekday()]+datetime.time(6)
            else:
               self.orarioStanzaVuota[i]=datetime.time.now()
            i+=1

    def getOrarioStanzaVuota(self):
        return self.orarioStanzaVuota[0],self.orarioStanzaVuota[1],self.orarioStanzaVuota[2],self.orarioStanzaVuota[3]

    def getStanzeOccupate(self):
        return self.stanzeOccupate[0],self.stanzeOccupate[1],self.stanzeOccupate[2],self.stanzeOccupate[3]