Oggetti

- Game:
Proprietà: 
deck: il mazzo/ i mazzi con cui si gioca. 
players: numero di giocatori che partecipano al gioco. 
fase_del_gioco: in che fase del gioco si è.

Metodi: 
new_game: iniziare una nuova partita. 
quit_game: chiudere una partita.

- Player:
Proprietà: 
name: nome del giocatore. 
Avatar: avatar del personaggio.
Hand: mano in corso.

- HumanPlayer(Player)
Proprietà:
chips: fish giocatore.
last_score: punteggio partita precedente.

Metodi:

- Dealer(Player)
Proprietà:

Metodi:
ritira_puntate: ritiro delle puntate fatte in quella mano.

- Hand:
Proprietà: 
cards: carte che compongono la mano.
score: valore attuale delle carte.

Metodi: 
add_card: aggiungi una carta alla mano. 
calcola_score: calcolare valore attuale dello score, NB: calcola sia il valore massimo che minimo possibile.
discard: scarta tutte le carte. 

 