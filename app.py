import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.game import Game

st.set_page_config(
   layout="wide",
)
card_width=95

number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)


st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
 deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)


pesca_button = st.button("Pesca una carta")
if pesca_button: 
   deck.draw()
st.image([card.image for drawn_card], width=card_width)

#prova rilancio su github





