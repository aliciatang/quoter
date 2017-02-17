import unittest
import quoter

class TestGetPrices(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(quoter.quote([]), [])

    def test_happy(self):
        res = quoter.quote(['Goog'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res['NASDAQ:GOOG'] > 0)

if __name__ == '__main__':
    unittest.main()
