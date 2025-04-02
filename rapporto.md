# 15.01.2025
Abbiamo deciso di programmare il gioco Black Jack. Abbiamo pensato a quali sono i passaggi fondamentali e necessari del gioco. 
Come prima cosa abbiamo scelto di inserire un pulsante che quando viene cliccato distribuisce la prima carta dal mazzo mescolato al giocatore, e la seconda al banco.
Stiamo creando l'oggetto Player; ad esso possiamo assegnare il valore della mano (che inizialmente è zero) e la quantità di soldi, che potrà variare in base alle modalità di gioco (split, raddoppia, ecc.)
Inoltre ad esso dovranno essere assegnate funzioni come quella di pescare la carta, accumularne i valori, e fermarsi. Non abbiamo ancora lavorato sull'interfaccia con streamlit. 
Probabilmente creeremo anche l'oggetto banco, che ha la principale differenza di dover sempre pescare un ulteriore carta quando il player sceglie di fermarsi. 
Stiamo lavorando su branch separate. 

# 22.01.2025
Abbiamo creato un file in cui abbiamo fatto la lista degli oggetti necessari (con le loro propiretà e metodi). E un altro in cui abbiamo scritto le fasi di gioco, che si svolgono a turni. Inoltre ne abbiamo fatto un altro in cui abbiamo marcato alcune cose che sarebbero interessanti da aggiungere. Ci siamo concentrati sul capire le regole e le varie possibilità di gioco.

# 29.1.2025
Andati avanti con la logica, e sistemato la fase 3 che può avere due esiti diversi (se il player sfora o pesca). 

# 5.2.2025
Oggi abbiamo terminato la descrizione scritta degli oggetti e iniziato a scrivere il codice di game, player, e hand ancora da sistemare. Rimane da valutare se creare l'oggetto phase e veramente necessario. Oltre a cio abbiamo rivisto l'organizzazione generale e alcune regole in vista della stesura del codice per la logica del gioco.

# 12.2.2025
Con l'aggiunta l'oggetto dealer_player e la scrittura di alcune altre funzioni come il conteggio dello score o il piazzamento delle puntate oggi abbiamo terminato la parte relativa alla creazione degli oggetti. Successivamente abbiamo riflettuto con il prof riguardo la logica generale del gioco e iniziato a scrivere il codice delle diverse fasi sotto l'oggetto game già definite nel file Fasi_gioco.
La parte grafica sara basata su queste fasi grazie all'impiego della funzione di streamlit session_state.

# 19.2.2025
Ho trovato un sito che spiega il session state con streamlit (vedi file "roba aggiuntiva"). Ho inizializzato l'oggetto game e aggiunto la funzione reset. Ho iniziato a provare su una branch a creare l'app con il session state. Devo ancora capire come far sparire gli elementi una volta finito l'intervallo dettato dal session state. Inoltre la prossima volta vorrei capire come integrare bene tutte le varie funzioni e fasi del gioco che attualmente sono distribuite nei vari oggetti. 

# 26.2.2025
Oggi abbiamo continuato a lavorare alla logica principale e l'interfaccia del gioco. Il lavoro è dipersé piuttosto scorrevole, ma abbiamo riscontrato diverse difficolta nel utilizzare la funzione session state.

# 12.3.2025
Oggi abbiamo lavorato interamente integrando la logica preparata in precedenza nell'interfaccia streamlit. Inizialmente abbiamo aggiunto il pulsante per la distribuzione delle carte e successivamente quello per pescarne delle altre o passare il turno. Nel fare cio siamo incappati in vari problemi riguardo la disposizione delle carte in due colonne e riguardo le fasi del gioco. Ora dovremo sistemare il fatto che le colonne di carte sono visibili sin dall'inizio del gioco e proseguire con le fasi.

# 2.4.2025
Dopo la parte teorica della lezione ci siamo concentrati sulle problematiche logiche e grafiche del gioco. In particolare il tasto "passa turno" non faceva si che il dealer pescasse le mancanti carte per raggiungere il punteggio di 17. Rimane ora da terminare con la logica e lavorare sulla grafica.
