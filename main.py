import random

class Domanda():
    def __init__(self, testo, livello, rispostag, input):
        self.testo = testo
        self.livello = livello
        self.rispostag = rispostag
        self.input = input

class Player():
    def __init__(self, nome):
        self.nome = nome
        self.punteggio = 0



class Game():
    def __init__(self, filePunti="punti.txt"):
        self.filePunti = filePunti

    def punteggioIniziale(self):
        #try:
           f =  open(self.filePunti, 'r', encoding='utf-8')
           line = f.readline()
           while line != "":
            pass

      #  excpet FileNotFoundError:
    def add_giocatore(self, giocatori=[]):
        giocatore = Player(input("inserisci il nome: "))
        giocatori.append(self.nome)
        return giocatore


    def leggiFile(self):
        pass





