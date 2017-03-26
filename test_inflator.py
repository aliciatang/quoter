import unittest
from datetime import datetime
from dateutil import relativedelta
import inflater

class TestWatcher(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(inflater.inflate({}), {})

    def test_less(self):
        monthAgo = (datetime.now() - relativedelta.relativedelta(months=1)).strftime('%Y/%m/%d')
        conf = {
            'ticker': { 'upper': 9000, 'lower': 8000, 'date': monthAgo, 'factor': '8%' },
            }
        conf = inflater.inflate(conf)
        inflate = conf['ticker']['inflate']
        self.assertTrue(inflate <  1.08)
        self.assertTrue(inflate >  1)
    def test_more(self):
        monthAgo = (datetime.now() - relativedelta.relativedelta(months=18)).strftime('%Y/%m/%d')
        conf = {
            'ticker': { 'upper': 9000, 'lower': 8000, 'date': monthAgo, 'factor': '8%' },
            }
        conf = inflater.inflate(conf)
        inflate = conf['ticker']['inflate']
        self.assertTrue(inflate >  1.08)
        self.assertTrue(inflate <  1.08**2)

if __name__ == '__main__':
    unittest.main()
