import unittest

from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 9)
        self.cardgame = CardGame
        self.cards = [self.card1, self.card2]

    def test_card_is_ace(self):
        

        self.assertEqual(True, self.cardgame.checkforAce(self, self.card1))

    def test_highest_card(self):

        self.assertEqual(self.card2, self.cardgame.highest_card(self, self.card1, self.card2))
    
    def test_cards_total(self):
        

        self.assertEqual("You have a total of 10", self.cardgame.cards_total(self.cards))