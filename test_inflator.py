import unittest
from datetime import datetime
from dateutil import relativedelta
import inflater

class TestWatcher(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(inflater.inflate({}), {})
        self.assertEqual(inflater.inflate({'date': '234'}), {'date': '234'})
        self.assertEqual(inflater.inflate({'factor': 'no'}), {'factor': 'no'})

    def test_less(self):
        monthAgo = (datetime.now() - relativedelta.relativedelta(months=1)).strftime('%Y/%m/%d')
        conf = {'date': monthAgo, 'factor': '8%'}
        conf = inflater.inflate(conf)
        inflate = conf['inflate']
        self.assertTrue(inflate <  1.08)
        self.assertTrue(inflate >  1)

    def test_more(self):
        monthAgo = (datetime.now() - relativedelta.relativedelta(months=18)).strftime('%Y/%m/%d')
        conf = {'date': monthAgo, 'factor': '8%'}
        conf = inflater.inflate(conf)
        inflate = conf['inflate']
        self.assertTrue(inflate >  1.08)
        self.assertTrue(inflate <  1.08**2)

if __name__ == '__main__':
    unittest.main()
