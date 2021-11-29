import unittest
from lib import quoter_yahoo as qy

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(qy.quote_yahoo([]), {})

    def test_happy(self):
        res = qy.quote_yahoo(['US.GOOG', 'US.BRK.A'])
        self.assertEqual(len(res), 2)
        self.assertTrue(res['US.GOOG'] > 0)
        self.assertTrue(res['US.BRK.A'] >20000)
    def test_expessive(self):
        res = qy.quote_yahoo(['US.BRK.A'])
        self.assertEqual(len(res), 2)
        self.assertTrue(res['US.BRK.A'] >20000)

    def test_unhappy(self):
        res = qy.quote_yahoo(['unhappy'])
        self.assertEqual(res, {})

    def test_mix(self):
        res = qy.quote_yahoo(['unhappy', 'US.BRK.B'])
        self.assertEqual(len(res), 2) # DUMMY GOOG will be added
        self.assertTrue(res['US.GOOG'] > 0)
        self.assertTrue(res['US.BRK.B'] > 0)
    def test_china(self):
        res = qy.quote_yahoo(['SZ.000651', 'SH.000001'])
        self.assertEqual(len(res), 2) # DUMMY GOOG will be added
        self.assertTrue(res['SZ.000651'] > 0)
        self.assertTrue(res['SH.000001'] > 0)


if __name__ == '__main__':
    unittest.main()
