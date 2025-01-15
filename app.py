import streamlit as st
from modules.card import Card
from modules.deck import Deck
#from modules.card import Player 

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
    shuffled_deck = deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)

cards= Card

if st.button("Pesca carta"):
    valore_mano= 0
    carta_pescata = st.image([cards[0] for card in deck.cards])  # pescare la prima carta
    valore_mano =+ card_scores  






