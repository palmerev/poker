import unittest

import pokerhand
import playingcards as pc
class TestStraight(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()

    def test_handtype(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('KC'), pc.Card('QD'), pc.Card('JD'), pc.Card('TH')
        ])
        self.assertEqual(self.hand1.handtype(), "Straight")

#    def test_ace_low(self):
#        self.hand2.cards.extend([
#            pc.Card('4D'), pc.Card('5C'), pc.Card('3C'), pc.Card('2H'), pc.Card('AH')
#        ])
#        self.assertEqual(self.hand2.handtype(), "Straight")

    def test_cmp_different_rank(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('KC'), pc.Card('QD'), pc.Card('JD'), pc.Card('TH')
        ])
        self.hand2.cards.extend([
            pc.Card('3D'), pc.Card('4C'), pc.Card('5C'), pc.Card('6H'), pc.Card('7H')
        ])
        self.assertGreater(self.hand1, self.hand2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
