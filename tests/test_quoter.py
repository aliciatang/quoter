import unittest
from lib.quoter import quote

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quote([]), {})

    def test_US(self):
        res = quote(['US.Goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['US.GOOG'] > 0)

    def test_expessive(self):
        res = quote(['US.BRK.A'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['US.BRK.A'] > 20000)

    def test_SH(self):
        res = quote(['SH.600004'])
        self.assertTrue(res['SH.600004'] > 0)

    def test_SZ(self):
        res = quote(['SZ.000651'])
        self.assertTrue(res['SZ.000651'] > 0)

    def test_HK(self):
        res = quote(['HK.02186'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['HK.02186'] > 0)

    def test_unhappy(self):
        res = quote(['SH.833330'])
        self.assertEqual(res, {})

    def test_mix(self):
        res = quote(['unhappy', 'US.goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['US.GOOG'] > 0)

if __name__ == '__main__':
    unittest.main()
