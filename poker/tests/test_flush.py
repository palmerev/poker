import unittest

import pokerhand
import playingcards as pc
class TestFlush(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()

    def test_is_flush(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('KH'), pc.Card('7H'), pc.Card('JH'), pc.Card('TH')
        ])
        self.assertEqual(self.hand1.handtype(), "Flush")

    def test_is_not_flush(self):
        self.hand1.cards.extend([
            pc.Card('AD'), pc.Card('KH'), pc.Card('7H'), pc.Card('JH'), pc.Card('TH')
        ])
        self.assertNotEqual(self.hand1.handtype(), "Flush")

    def test_cmp_different_rank(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('KH'), pc.Card('7H'), pc.Card('JH'), pc.Card('TH')
        ])
        self.hand2.cards.extend([
            pc.Card('KC'), pc.Card('4C'), pc.Card('5C'), pc.Card('QC'), pc.Card('7C')
        ])
        self.assertGreater(self.hand1, self.hand2)

    def test_cmp_same_rank(self):
        self.hand1.cards.extend([
            pc.Card('AH'), pc.Card('KH'), pc.Card('7H'), pc.Card('JH'), pc.Card('TH')
        ])
        self.hand2.cards.extend([
            pc.Card('AC'), pc.Card('KC'), pc.Card('7C'), pc.Card('JC'), pc.Card('TC')
        ])
        self.assertEqual(self.hand1, self.hand2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
