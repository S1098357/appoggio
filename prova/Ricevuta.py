import datetime
import pickle


class Ricevuta():

    def __init__(self):
        self.prezzo
        self.dataRilascio=datetime.date

    def salva(self,prezzo):
        self.prezzo=prezzo
        self.dataRilascio=datetime.date.today()
        dizio={
            'importo:':self.prezzo,
            'data rilascio:':self.dataRilascio
        }
        with open ('dati/Ricevuta.pickle' , 'wb+') as f:
            pickle.dump(dizio,f,pickle.HIGHEST_PROTOCOL)

    def stampa(self):
        if open('dati/Ricevuta.pickle', 'rb') :
            with open('dati/Ricevuta.pickle', 'rb') as f:
                dizio = pickle.load(f)
                LeggiRicevutaGUI(dizio['importo'],dizio['data rilascio'])
