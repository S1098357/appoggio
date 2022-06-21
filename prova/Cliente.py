import datetime

#from PyQt5.uic.properties import QtWidgets

#from Amministrazione.Sistema import Sistema
from nis import match

from Amministrazione import Sistema
from Amministrazione.Segreteria import Segreteria
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from datetime import timedelta
from datetime import datetime
from Servizio import Prenotazione

from GUI.SelezionaPrenotazioneGUI import SelezionaPrenotazioneGUI
from GUI.VisualizzaDottoreGUI import VisualizzaDottoreGUI
from GUI.VisualizzaPrenotazioneGUI import VisualizzaPrenotazioneGUI


class Cliente:
    def __init__(self):
        self.nomeCognome = ""
        self.nomeDottore = ""
        self.password = ""
        self.email = ""
        self.numeroDiTelefono = ""
        self.codiceFiscale = ""
        self.id = 0
        self.messaggio = []
        self.prenotazione = Prenotazione
        self.promemoria
        self.listaPrenotazioniCliente = []


    def inserisciNomeCognome (self, nome):
           if nome.isalpha() :
                self.nomeCognome = nome
                return True
           else :
                return False

    def inserisciEmail (self, email):
        if "@" in email:
            stringa1, stringa2 = email.split("@")
            if "." in stringa2:
                self.email = email
                return True
        return False

    def inserisciNumeroDiTelefono (self, numeroDiTelefono):
        if numeroDiTelefono.isdecimal():
            self.numeroDiTelefono = numeroDiTelefono
            return True
        else:
            return False

    def inserisciCodiceFiscale (self, codiceFiscale):
        c=0
        y=0
        for x in codiceFiscale:
            if x.isalpha:
                c+=1
            if x.isdecimal:
                y+=1
        if c==9 and y==7:
            self.codiceFiscale = codiceFiscale
            return True
        else :
            return False

    def dizio(self):
        return {
        'nome ':self.nomeCognome,
        'doc':self.nomeDottore,
        'pass':self.password,
        'email':self.email ,
        'num.Tel':self.numeroDiTelefono ,
        'codice fisc.':self.codiceFiscale ,
        'id':self.id,
        'msg':self.messaggio ,
        'prenotazione':self.prenotazione,
        'promemoria':self.promemoria,
        'lista':self.listaPrenotazioniCliente
        }

    def inserisciPassword (self, password):
        self.password = password

    def selezionaMedico (self, nomeDottore):
        self.nomeDottore = nomeDottore

    def setId (self, id):
        self.id=id

    def getId (self):
        return self.id

    def getEmail (self):
        return self.email

    def getNomeCognome (self):
        return self.nomeCognome

    def getNumeroDiTelefono (self):
        return self.numeroDiTelefono

    def registrazione (self,flag):
        nome,nomeDottore,password,email,numTelefono,codiceFiscale,CC=RegistrazioneGUI(flag)
        cartellaClinica=CartellaClinica()
        if self.inserisciNomeCognome(nome) and self.inserisciEmail(email) and self.inserisciNumeroDiTelefono(numTelefono) and self.inserisciCodiceFiscale(codiceFiscale):
            cartellaClinica.id=self.id
            cartellaClinica.patologie=CC
            cartellaClinica.stampaCartella()
            self.inserisciPassword(password)
            self.selezionaMedico(nomeDottore)
            Segreteria.salvaClienti()
        else:
            self.registrazione(True)

    def richiediPrenotazione(self, listaPrenotazioni, listaDottori):
        self.prenotazione = Prenotazione
        giorno=selezionaGiornoGUI()
        #delta = datetime.time(minute=15)
        lista=[]
        for dottore in listaDottori:
            if dottore.nomeCognome == self.nomeDottore:
                lista.append(dottore.orarioLavoro[giorno.weekday()])
        for k in range(0, 23):
            lista.append(lista[len(lista)-1]+ timedelta(minutes=15))
        listaPrenotate = []
        for prenotazione in listaPrenotazioni:
            listaPrenotate.append(prenotazione.dataOra)
        listaFinale = lista - listaPrenotate
        pren =self.prenotazione()
        appoggio = NuovaPrenotazioneGUI(listaFinale)
        if appoggio.stampa()!=None:
            pren.dataOra,tipo, pren.note = appoggio.stampa()
            if tipo=='Certificato':
                pren.certificatoMedico = True
            elif tipo=='Ricetta':
                pren.ricettaMedica=True
            else:
                pren.visitaGenerica= True
            pren.cliente=self.nomeCognome
            pren.dottore=self.nomeDottore
            Sistema.listaPrenotazioni.append(pren)
            Sistema.salvaPrenotazioni(pren.stampaPrenotazione)
        self.menuCliente()




    def selezionaDataOra(self,listaPrenotazioni, listaDottori):
        delta=datetime.time(minute=15)
        lista2 = []
        for dottore in listaDottori:
            if dottore.nomeCognome==self.nomeDottore:
                lista =dottore.orarioLavoro
        for contatore in range (0,24) :
            contatore += 1
            lista.append(lista.index(contatore)+delta)
            listaPrenotate=0
        for prenotazione in listaPrenotazioni:
            listaPrenotate.append(prenotazione.dataOra)
        listaFinale = lista-listaPrenotate

        # self.prenotazione.orario=Grafica.show(listaFinale)


    def promemoria (self):
        if (Sistema.invioPromemoria(self.listaPrenotazioniCliente)):
            self.promemoria = "Il tuo appuntamento è domani"

    def eliminaPrenotazione(self,prenotazione,sistema):
        for elem in sistema.listaPrenotazioni:
            if elem==prenotazione:
                sistema.listaPrenotazioni.remove(prenotazione)
        sistema.salvaPrenotazioni()

    def visualizzaPrenotazione(self,listaPrenotazioni):
        lista=[]
        for prenotazione in listaPrenotazioni:
            if prenotazione.cliente==self.nomeCognome:
                lista.append(prenotazione)
        pren=SelezionaPrenotazioneGUI(lista)
        if pren!=None:
            VisualizzaPrenotazioneGUI(pren)

    def visualizzaInfoMedico(self,listaDottori):
        for dottore in listaDottori:
            if dottore.nomeCognome==self.nomeDottore:
                VisualizzaDottoreGUI(dottore)

    def menuCliente(self,sistema,listaDottori,listaPrenotazioni):
        while True:
            risposta=MenuClienteGUI()
            match risposta:
                case 0:
                    self.richiediPrenotazione(sistema.listaPrenotazioni,listaDottori)
                case 1:
                    prenotazione=SelezionaPrenotazioneGUI(listaPrenotazioni)
                    self.eliminaPrenotazione(prenotazione,sistema)
                case 2:
                    prenotazione = SelezionaPrenotazioneGUI(listaPrenotazioni)
                    self.eliminaPrenotazione(prenotazione, sistema)
                    self.richiediPrenotazione(sistema.listaPrenotazioni,listaDottori)
                case 3:
                    self.visualizzaPrenotazione(listaPrenotazioni)
                case 4:
                    self.visualizzaInfoMedico(listaDottori)
