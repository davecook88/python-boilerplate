from enum import Enum


class CardSuit(Enum, str):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class Card:
    value: str
