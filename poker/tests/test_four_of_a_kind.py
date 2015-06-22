import unittest

import pokerhand #imports playingcards
import playingcards as pc
class TestFourOfAKind(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()

    def test_handtype_sorted(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('AD'), pc.Card('AH'), pc.Card('4H')
        ])
        self.assertEqual(self.hand1.handtype(), "Four of a Kind")

    def test_handtype_unsorted(self):
        self.hand2.cards.extend([
            pc.Card('3D'), pc.Card('3S'), pc.Card('3C'), pc.Card('KH'), pc.Card('3H')
        ])
        self.assertEqual(self.hand2.handtype(), "Four of a Kind")

    def test_cmp_different_group_rank(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('AD'), pc.Card('AS'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('3D'), pc.Card('3S'), pc.Card('3C'), pc.Card('KH'), pc.Card('3H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_aces_vs_kings(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('AD'), pc.Card('AS'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('KS'), pc.Card('KC'), pc.Card('KH'), pc.Card('KD'), pc.Card('3H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_queens_vs_kings(self):
        self.hand1.cards.extend([
            pc.Card('QH'), pc.Card('QC'), pc.Card('QD'), pc.Card('QS'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('KS'), pc.Card('KC'), pc.Card('KH'), pc.Card('KD'), pc.Card('3H')
        ])
        self.assertGreater(self.hand2, self.hand1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
