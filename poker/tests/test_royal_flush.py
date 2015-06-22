import unittest

import pokerhand
import playingcards as pc
class TestRoyalFlush(unittest.TestCase):
    def setUp(self):
        self.hand1 = pokerhand.Hand()
        self.hand2 = pokerhand.Hand()

    def tearDown(self):
        self.hand1.discard_all()
        self.hand2.discard_all()
        self.hand1 = None
        self.hand2 = None

    def test_is_royal_flush(self):
        self.hand1.cards.extend([
            pc.Card('KH'), pc.Card('QH'), pc.Card('JH'), pc.Card('TH'), pc.Card('AH')
        ])
        self.assertEqual(self.hand1.handtype(), "Royal Flush")

if __name__ == '__main__':
    unittest.main(verbosity=2)
