import unittest

import pokerhand
import playingcards as pc
class TestStraightFlush(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()
        self.hand1 = None
        self.hand2 = None
        
    def test_nine_to_king(self):
        self.hand1.cards.extend([
            pc.Card('KH'), pc.Card('QH'), pc.Card('JH'), pc.Card('TH'), pc.Card('9H')
        ])
        self.assertEqual(self.hand1.handtype(), "Straight Flush")

    def test_two_to_six(self):
        self.hand1.cards.extend([
            pc.Card('2H'), pc.Card('3H'), pc.Card('4H'), pc.Card('5H'), pc.Card('6H')
        ])
        self.assertEqual(self.hand1.handtype(), "Straight Flush")

    def test_ace_low(self):
        self.hand2.cards.extend([
            pc.Card('4C'), pc.Card('5C'), pc.Card('3C'), pc.Card('2C'), pc.Card('AC')
        ])
        self.assertEqual(self.hand2.handtype(), "Straight Flush")

    def test_cmp_different_rank(self):
        self.hand1.cards.extend([
            pc.Card('KH'), pc.Card('QH'), pc.Card('JH'), pc.Card('TH'), pc.Card('9H')
        ])
        self.hand2.cards.extend([
            pc.Card('2D'), pc.Card('3D'), pc.Card('4D'), pc.Card('5D'), pc.Card('6D')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_same_rank(self):
        self.hand1.cards.extend([
            pc.Card('KH'), pc.Card('QH'), pc.Card('JH'), pc.Card('TH'), pc.Card('9H')
        ])
        self.hand2.cards.extend([
            pc.Card('KD'), pc.Card('QD'), pc.Card('JD'), pc.Card('TD'), pc.Card('9D')
        ])
        self.assertEqual(self.hand1, self.hand2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
