import unittest
from lib import quoter

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quoter.quote([]), {})

    def test_happy(self):
        res = quoter.quote(['US.Goog', 'US.BRK.A'])
        self.assertTrue(res['US.GOOG'] > 0)
        self.assertTrue(res['US.BRK.A'] >20000)

    def test_expessive(self):
        res = quoter.quote(['US.BRK.A'])
        self.assertTrue(res['US.BRK.A'] >20000)

    def test_unhappy(self):
        res = quoter.quote(['unhappy'])
        self.assertEqual(res, {})

    def test_mix(self):
        res = quoter.quote(['unhappy', 'US.BRK.A'])
        self.assertTrue(res['US.BRK.A'] > 0)

if __name__ == '__main__':
    unittest.main()
