from datetime import datetime

from GUI.AggiornaCCGUI import AggiornaCCGUI
from GUI.CompilaCertificatoGUI import CompilaCertificatoGUI
from GUI.CompilaRicettaGUI import CompilaRicettaGUI
from GUI.MenuDottoreGUI import MenuDottoreGUI
from GUI.VisualizzaCCGUI import VisualizzaCCGUI
from GUI.VisualizzaTuttePrenotazioniGUI import VisualizzaTuttePrenotazioniGUI
from prova.Cliente import Cliente
from prova.Segreteria import Segreteria


class Dottore:

    def __init__(self,nomeCognome,numTelefono):
        self.clienteAttuale=Cliente()
        self.listaPrenotazioniOggi=[]
        self.nomeCognome=nomeCognome
        self.numeroDiTelefono=numTelefono
        self.OrarioLavoro=[]
        self.listaCartelleCliniche=[]
        self.documento

    def ricercaCartellaClinica(self,id):
        for CC in self.listaCartelleCliniche:
            if CC.GetId==id:
                return CC

    def aggiornaCartellaClinica(self):
        CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
        appoggio=(AggiornaCCGUI(CC.patologie))
        if appoggio!=None:
            CC.setPatologie(appoggio)
            CC.stampaCartella()

    def chiamaClienteSuccessivo(self):
        for prenotazione in self.listaPrenotazioniOggi:
            if prenotazione.nomeCliente==self.clienteAttuale.nomeCognome:
                prenAttuale=prenotazione
                if prenotazione==self.listaPrenotazioniOggi[len(self.listaPrenotazioniOggi)-1]:
                    self.clienteAttuale=None
                else:
                    appoggio=self.listaPrenotazioniOggi[self.listaPrenotazioniOggi.index(prenotazione)+1]
                    self.ClienteAttuale=Segreteria.ricercaCliente(appoggio.nomeCliente)
        self.listaPrenotazioniOggi.remove(prenAttuale)

    #def compilaCertificato(self):
     #   tipo=grafica.tipoCertificato()
     #   if tipo=='certificato di malattia':
      #      self.documento=CertificatoMalattia()
       # else:
        #    if tipo=='certificato sana e robusta costituzione'
         #       self.documento=CertificatoSanaERobustaCostituzione()
          #  else:
           #     self.documento=CertificatoAgoistico()
        #self.certificatoMedico.compilaCertificato(self.nomeCognome, self.clienteAttuale.nomeCognome, datetime.now())

    #def prescriviFarmaco(self):
        #self.documento.compilaRicetta(self.clienteAttuale.nomeCognome,self.nomeCognome,datetime.now(),grafica.compilaRicetta())

    #def setDataOraLavoro(self):
       # self.orarioLavoro.append(grafica.scegliOrario())

    def visualizzaCartellaClienteAttuale(self):
        CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
        VisualizzaCCGUI(CC.patologie)

    def visualizzaPrenotazioni(self):
        VisualizzaTuttePrenotazioniGUI(self.listaPrenotazioniOggi)

    def ricercaPrenotazioneOggi(self,listaPrenotazioni):
        for prenotazione in listaPrenotazioni:
            if prenotazione.dataOra.day==datetime.today().day:
                self.listaPrenotazioniOggi.append(prenotazione)


    def menuDottore(self):
        risposta=MenuDottoreGUI(self.clienteAttuale.nomeCognome)
        while True:
            match risposta:
                case 0:
                    cliente,tipo,prezzo=CompilaCertificatoGUI(self.clienteAttuale,self.nomeCognome)
                    match tipo:
                        case 'certificato agonistico':
                            self.documento=CertificatoMedicoAgonistico()
                        case 'certificato malattia':
                            self.documento=CertificatoMalattia()
                        case 'sana e robusta costituzione':
                            self.documento=CertificatoSanaRobustaCostituzione()
                    if self.documento!=None:
                        self.documento.compilaCertificato(cliente,self.nomeCognome,datetime.today())
                        self.documento.stampa()
                case 1:
                    cliente,farmacoPrescritto=CompilaRicettaGUI(self.nomeCognome,self.clienteAttuale)
                    if cliente!=None and farmacoPrescritto!=None:
                        self.documento=Ricetta()
                        self.documento.compilaRicetta(farmacoPrescritto,cliente,self.nomeCognome,datetime.today())
                        self.documento.stampa()
                case 3:
                    self.chiamaClienteSuccessivo()
                    self.menuDottore()
                case 5:
                    self.visualizzaPrenotazioni()
                case 2:
                    self.aggiornaCartellaClinica()
                case 4:
                    self.visualizzaCartellaClienteAttuale()

    def dottorePre(self,listaPrenotazioni,listaClienti):
        self.ricercaPrenotazioneOggi(listaPrenotazioni)
        if self.listaPrenotazioniOggi!=None:
            for cliente in listaClienti:
                if cliente.nomeCognome==self.listaPrenotazioniOggi[0].nomeCliente:
                    self.clienteAttuale=cliente
            self.menuDottore()
        else:
            self.clienteAttuale=None