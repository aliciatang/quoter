import unittest
import quoter

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quoter.quote([]), None)

    def test_happy(self):
        res = quoter.quote(['Goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['GOOG'] > 0)

    def test_expessive(self):
        res = quoter.quote(['BRK.A'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['BRK.A'] > 20000)

    def test_unhappy(self):
        res = quoter.quote(['unhappy'])
        self.assertEqual(res, None)

    def test_mix(self):
        res = quoter.quote(['unhappy', 'goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['GOOG'] > 0)

if __name__ == '__main__':
    unittest.main()
