import unittest

import pokerhand
import playingcards as pc
class TestFullHouse(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()

    def test_aces_over_tens(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('AD'), pc.Card('TD'), pc.Card('TH')
        ])
        self.assertEqual(self.hand1.handtype(), "Full House")

    def test_tens_over_aces(self):
        self.hand1.cards.extend([
            pc.Card('TH'), pc.Card('TC'), pc.Card('TD'), pc.Card('AD'), pc.Card('AH')
        ])
        self.assertEqual(self.hand1.handtype(), "Full House")

    def test_cmp_different_rank(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('AD'), pc.Card('TD'), pc.Card('TH')
        ])
        self.hand2.cards.extend([
            pc.Card('KD'), pc.Card('KC'), pc.Card('KH'), pc.Card('7D'), pc.Card('7H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_cmp_higher_pair(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('TC'), pc.Card('TD'), pc.Card('TH')
        ])
        self.hand2.cards.extend([
            pc.Card('7D'), pc.Card('7C'), pc.Card('7H'), pc.Card('AD'), pc.Card('AS')
        ])
        self.assertGreater(self.hand1, self.hand2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
