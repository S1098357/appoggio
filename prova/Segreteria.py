import datetime
import os
import pickle

from Amministrazione.Calendario import Calendario
from Amministrazione.Sistema import Sistema

from GUI.AnnuncioMessaggioGUI import AnnuncioMessaggioGUI
from GUI.EliminaCCGUI import EliminaCCGUI
from GUI.MenuSegreteriaGUI import MenuSegreteriaGUI
from GUI.RUDClienteGUI import RUDClienteGUI
from GUI.RUDPrenotazioneGUI import RUDPrenotazioneGUI
from GUI.SceltaPrenotazioneGUI import SceltaPrenotazioneGUI
from GUI.SelezionaPrenotazioneGUI import SelezionaPrenotazioneGUI
from GUI.StampaDocumentiGUI import StampaDocumentiGUI
from GUI.VisualizzaPrenotazioneGUI import VisualizzaPrenotazioneGUI
from Servizio.Dottore import Dottore

from GUI.AnnuncioGUI import AnnuncioGUI
from GUI.CompilaRicevutaGUI import CompilaRicevutaGUI
from GUI.MessaggioGUI import MessaggioGUI
from GUI.ModificaClienteGUI import ModificaClienteGUI
from GUI.SceltaVisualizzaClienteGUI import SceltaVisualizzaClienteGUI
from GUI.SelezionaClienteGUI import SelezionaClienteGUI
from GUI.SelezionaDottoreGUI import SelezionaDottoreGUI
from GUI.SelezionaGiornoGUI import SelezionaGiornoGUI
from GUI.StampaCertificatoGUI import StampaCertificatoGUI
from GUI.StampaRicettaGUI import StampaRicettaGUI
from GUI.VisualizzaClienteSingoloGUI import VisualizzaClienteSingoloGUI
from GUI.VisualizzaClientiListaGUI import VisualizzaClientiListaGUI
from GUI.VisualizzaStanze import VisualizzaStanze
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from prova.CertificatoMedico import CertificatoMedico
from prova.Cliente import Cliente
from prova.Ricevuta import Ricevuta


class Segreteria:

    def _init_(self):
        self.listaClienti=[]
        self.listaDottori=[]
        self.leggiOrario()
        self.username="segreteria"
        self.password="1234578"
        self.x=Sistema
        self.appoggioPrezzo=0
        self.calendario=Calendario()

    def ricercaPrenotazioneData(self,data,listaPrenotazioni):
        listaOdierna=[]
        for prenotazione in listaPrenotazioni:
            if prenotazione.dataOra.date==data:
                listaOdierna.append(prenotazione)
            elif prenotazione.dataOra.date<data:
                self.eliminaPrenotazione(listaPrenotazioni,prenotazione)
        return listaOdierna

    def eliminaPrenotazione(self,prenotazione):
        for elem in self.x.listaPrenotazioni:
            if elem==prenotazione:
                self.x.listaPrenotazioni.remove(prenotazione)
        self.x.salvaPrenotazioni()

    def aggiornaStatoClinica(self):
        data = datetime.datetime.today()
        listaOdierna = self.ricercaPrenotazioneData(data.date,self.x.listaPrenotazioni)
        Dottore.listaPrenotazioni = listaOdierna

    def compilaRicevuta(self):
        prezzo = CertificatoMedico.leggiCertificato()
        if prezzo!=None:
            x=CompilaRicevutaGUI()
            if x == True:
                Ricevuta.salva (prezzo)

    def eliminaCartellaClinica(self,id):
        os.remove('dati/CC/cartella' + str(self.id) + '.pickle')

    def inviaMessaggioSingolo(self):
        messaggio, nome = MessaggioGUI(self.listaClienti)
        if messaggio!=None and nome!=None:
            for cliente in self.listaClienti:
                if cliente.nome == nome:
                    cliente.messaggio.append(messaggio)
        else:
            self.menuSegreteria()

    def salvaClienti(self):
        appoggio={}
        for cliente in self.listaClienti:
            appoggio+=cliente.dizio()
        with open('dati/Clienti.pickle', 'wb+') as f:
            pickle.dump(appoggio, f, pickle.HIGHEST_PROTOCOL)

    def leggiClienti(self):
        if os.path.isfile('dati/Clienti.pickle'):
            with open('dati/Clienti.pickle', 'rb+') as f:
                self.listaClienti = pickle.load(f)
        else:
            self.errore()

    def ricercaCliente(self,cliente):
        for elem in self.listaClienti:
            if elem.nomeCognome==cliente:
                return elem

    def modificaCliente(self):
        appoggio=Cliente()
        appoggio.nomeCognome, appoggio.email, appoggio.numTelefono = None
        while appoggio.nomeCognome== None and appoggio.email == None and appoggio.numTelefono == None:
            cliente=SelezionaClienteGUI(self.listaClienti)
            if cliente!=None:
                appoggio=self.ricercaCliente(cliente)
                self.listaClienti.remove(appoggio)
                appoggio.nomeCognome, appoggio.email,appoggio.numTelefono=ModificaClienteGUI(cliente)
            else:
                appoggio.nomeCognome='aaa'
                self.menuSegreteria()
        self.listaClienti.append(appoggio)
        self.salvaClienti()


    def eliminaCliente(self):
        cliente = SelezionaClienteGUI(self.listaClienti)
        self.listaClienti.remove(self.ricercaCliente(cliente))
        self.salvaClienti()

    def modificaOrarioDottore(self):
        giorno=None
        appoggio=None
        while giorno==None and appoggio==None:
            dottore = SelezionaDottoreGUI(self.listaDottori)
            if dottore!=None:
                giorno,appoggio = SelezionaGiornoGUI()
            else:
                giorno=2
                self.menuSegreteria()
        self.listaDottori[dottore].OrarioLavoro[giorno]=appoggio
        self.salvaOrario()
        self.menuSegreteria()

    def salvaOrario(self):
        dizio={}
        i=0
        for i in range (0,3):
            for j in range (0,5):
                dizio+={'orario dottore'+ i+1 + 'giorno' + j:self.listaDottori[i].OrarioLavoro[j] }
                i+1
        with open('dati/orari.pickle', 'wb+') as f:
            pickle.dump(dizio, f, pickle.HIGHEST_PROTOCOL)

    def leggiOrario(self):
        if os.path.isfile('dati/orari.pickle'):
            with open('dati/orari.pickle', 'rb+') as f:
                appoggio = pickle.load(f)
            for i in range (0,3):
                for j in range(0, 5):
                    self.listaDottori[i].OrarioLavoro[j]=appoggio['orario dottore'+ i+1 + 'giorno' + j]
        else:
            for i in range(0, 3):
                for j in range(0, 5):
                    self.listaDottori[i].OrarioLavoro[j] = datetime.time(hour=10,minute=0)

    def pubblicaAnnuncio(self):
        annuncio=AnnuncioGUI()
        if annuncio!=None:
            dizio={'annuncio': annuncio}
            with open('dati/annunci.pickle', 'wb+') as f:
                pickle.dump(dizio, f, pickle.HIGHEST_PROTOCOL)
        else:
            self.menuSegreteria()

    def leggiAnnuncio(self):
        if os.path.isfile('dati/annunci.pickle'):
            with open('dati/annunci.pickle', 'rb+') as f:
                messaggio = pickle.load(f)
            for cliente in self.listaClienti:
                cliente.messaggio.append(messaggio)

    def leggiCertificato(self):
        if os.path.isfile('dati/Certificati.pickle'):
            with open('dati/Certificati.pickle', 'rb+') as f:
                certificato = pickle.load(f)
            StampaCertificatoGUI(certificato)
            self.menuSegreteria()
        else :
            self.errore()

    def leggiRicetta(self):
        if os.path.isfile('dati/Ricetta.pickle'):
            with open('dati/Ricetta.pickle', 'rb+') as f:
                ricetta = pickle.load(f)
            StampaRicettaGUI(ricetta)
            self.menuSegreteria()
        else :
            self.errore()

    def visualizzaCliente(self):
        risposta=SceltaVisualizzaClienteGUI()
        listaClientiDottore=[]
        if risposta == True:
            dottoreSelezionato=SelezionaDottoreGUI()
            for cliente in self.listaClienti:
                if cliente.nomeDottore==dottoreSelezionato:
                    listaClientiDottore.append(cliente)
            VisualizzaClientiListaGUI(listaClientiDottore)
            self.menuSegreteria()
        else:
            cliente=SelezionaClienteGUI(self.listaClienti)
            if cliente!=None:
                VisualizzaClienteSingoloGUI(cliente)
                self.menuSegreteria()

    def visualizzaStanze(self):
        VisualizzaStanze(self.calendario.getStanzeOccupate(),self.calendario.getOrarioStanzaVuota())
        self.menuSegreteria()

    def visualizzaPrenotazione(self):
        risposta=SceltaPrenotazioneGUI()
        listaPrenotazioni=[]
        if risposta == True:
            dottoreSelezionato=SelezionaDottoreGUI()
            for prenotazione in self.x.listaPrenotazioni:
                if prenotazione.dottore==dottoreSelezionato:
                    listaPrenotazioni.append(prenotazione)
            VisualizzaTuttePrenotazioniGUI(listaPrenotazioni)
        elif risposta==False:
            prenotazione=SelezionaPrenotazioneGUI(listaPrenotazioni)
            if prenotazione!=None:
                VisualizzaPrenotazioneGUI(prenotazione)
        self.menuSegreteria()

    def menuSegreteria(self):
        while True:
            risposta=MenuSegreteriaGUI()
            match risposta:
                case 0:
                    id=EliminaCCGUI()
                    self.eliminaCartellaClinica(id)
                case 1:
                    risposta2=StampaDocumentiGUI()
                    match risposta2:
                        case 0:
                            self.leggiRicetta()
                        case 1:
                            self.leggiCertificato()
                        case 2:
                            Ricevuta.stampa()
                case 2:
                    risposta2 = RUDPrenotazioneGUI()
                    if risposta2==True:
                        prenotazione=SelezionaPrenotazioneGUI()
                        self.eliminaPrenotazione(prenotazione)
                    elif risposta==False:
                        self.visualizzaPrenotazione()
                case 3:
                    risposta2=RUDClienteGUI()
                    match risposta2:
                        case 0:
                            self.visualizzaCliente()
                        case 1:
                            self.modificaCliente()
                        case 2:
                            self.eliminaCliente()
                case 4:
                    self.modificaOrarioDottore()
                case 5:
                    self.visualizzaStanze()
                case 6:
                    self.compilaRicevuta()
                case 7:
                    risposta2=AnnuncioMessaggioGUI()
                    if risposta2==True:
                        self.pubblicaAnnuncio()
                    elif risposta2==False:
                        self.inviaMessaggioSingolo()

