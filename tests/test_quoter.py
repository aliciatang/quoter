import unittest
import env
from lib.quoter import quote

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quote([]), None)

    def test_happy(self):
        res = quote(['Goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['GOOG'] > 0)

    def test_expessive(self):
        res = quote(['BRK.A'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['BRK.A'] > 20000)

    def test_unhappy(self):
        res = quote(['unhappy'])
        self.assertEqual(res, None)

    def test_mix(self):
        res = quote(['unhappy', 'goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['GOOG'] > 0)

if __name__ == '__main__':
    unittest.main()
