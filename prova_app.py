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

if 'phase' not in st.session_state:
    st.session_state.phase = False

if 'game_obj' not in st.session_state:
    st.session_state.game_obj =None 

if not st.session_state.game:
    if st.button('Inizia il gioco'):
        st.session_state.game = True 
        st.session_state.phase= "scegli_num_mazzi"



if st.session_state.phase == "scegli_num_mazzi":
    number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1) 
    if st.button("Conferma mazzi"): 
        st.session_state.game_obj = Game(number_of_decks)
        st.markdown(f"## Mazzo creato con {number_of_decks} mazzo/i")
        st.session_state.phase= "scommesse (fase1)"

game: Game = st.session_state.game_obj

if st.session_state.phase == "scommesse (fase1)":
    st.subheader("Fai la tua puntata:")
    bet= st.number_input("Inserisci la tua puntata:", min_value=50, max_value= 10000, step= 50) #da sostituire il max con le chips che ha il giocatore!!!
    if st.button("Piazza la puntata"): 
            st.session_state.current_bet = bet 
            st.success(f"Puntata di {bet} accettata!")
            st.session_state.phase = "distribuzione (fase2)"

if st.session_state.phase == "distribuzione (fase2)":
    if st.button("Distribuzione carte:"):

        game.player.hand.add_card(game.deck.draw())
        game.player.hand.add_card(game.deck.draw())
        game.dealer.hand.add_card(game.deck.draw())


        st.session_state.phase= "player turn (fase3)"

        
if st.session_state.phase != "scommesse (fase1)" and st.session_state.phase !="scegli_num_mazzi" and st.session_state.game != False :
    col1, col2= st.columns(2)

    with col1:
        st.header("Carte Player")
        st.image([card.image for card in game.player.hand.cards], width=100)
    # st.image(player_card2.image, width=100)



    with col2:
        st.header("Carte Dealer")
        st.image([card.image for card in game.dealer.hand.cards], width=100)
    


if st.session_state.phase == "player turn (fase3)" :
    if st.button("Pesca"):
        game.player.hand.add_card(game.deck.draw())
        st.rerun()
        
    if st.button("Passa"):
        st.session_state.phase= "dealer turn (fase4)"
   


def dealer_turn():
    st.write("Turno Dealer")

    game.dealer.hand.add_card(game.deck.draw())
    st.session_state.phase= "calcolo punteggi (fase5)"
    st.rerun()


if st.session_state.phase == "dealer turn (fase4)":
    st.write("dealer turn")
