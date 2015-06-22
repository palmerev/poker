import unittest

import pokerhand #imports playingcards
import playingcards as pc
class TestTwoPair(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()

    def test_handtype_sorted(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('KD'), pc.Card('KD'), pc.Card('4H')
        ])
        self.assertEqual(self.hand1.handtype(), "Two Pair")

    def test_handtype_unsorted(self):
        self.hand2.cards.extend([
            pc.Card('3D'), pc.Card('3C'), pc.Card('5C'), pc.Card('5H'), pc.Card('2H')
        ])
        self.assertEqual(self.hand2.handtype(), "Two Pair")

    def test_two_different_pairs(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('5D'), pc.Card('5H'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('3D'), pc.Card('5C'), pc.Card('KC'), pc.Card('KH'), pc.Card('3H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_same_top_pair(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AC'), pc.Card('KD'), pc.Card('KH'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('AS'), pc.Card('AD'), pc.Card('QH'), pc.Card('QD'), pc.Card('3H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_same_two_pairs(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AD'), pc.Card('QH'), pc.Card('QD'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('AS'), pc.Card('AC'), pc.Card('QS'), pc.Card('QC'), pc.Card('3H')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_equal_two_pair(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('AD'), pc.Card('QH'), pc.Card('QD'), pc.Card('4H')
        ])
        self.hand2.cards.extend([
            pc.Card('AS'), pc.Card('AC'), pc.Card('QS'), pc.Card('QC'), pc.Card('4S')
        ])
        self.assertEqual(self.hand1, self.hand2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
