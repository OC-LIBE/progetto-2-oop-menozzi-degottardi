import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.game import Game
from modules.player import Player
from modules.human_player import HumanPlayer
from modules.dealer_player import Dealerplayer
from modules.hand import Hand 


st.title("BlackJack")

if 'game' not in st.session_state:
    st.session_state.game = False
    st.session_state.game_obj=Game(3)
    
game:Game=st.session_state.game_obj


if not st.session_state.game:
    if st.button('Inizia il gioco'):
        st.session_state.game = True 
        st.session_state.phase= "scegli_num_mazzi"



if st.session_state.phase == "scegli_num_mazzi":
    number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1) 
    deck = Deck(number_of_decks)
    if st.button("Conferma mazzi"): 
        st.markdown(f"## Mazzo creato con {number_of_decks} mazzo/i")
        st.session_state.phase= "scommesse"

if st.session_state.phase == "scommesse":
    st.subheader("Fai la tua puntata:")
    bet= st.number_input("Inserisci la tua puntata:", min_value=0, max_value= 10000, step= 50) #da sostituire il max con le chips che ha il giocatore!!!
    if st.button("Piazza la puntata"): 
            st.session_state.current_bet = bet 
            st.success(f"Puntata di {bet} accettata!")
            st.session_state.phase = "distribuzione (fase1)"

if st.session_state.phase == "distribuzione (fase1)":
     player_card1= game.deck.draw()
     player_card2= game.deck.draw()
     dealer_card= game.deck.draw()
     
     game.player.hand.add_card(player_card1)
     game.player.hand.add_card(player_card2)
     game.player.hand.add_card(dealer_card)

     for card in game.player.hand.cards:
          st.image(card.image, width=100)








