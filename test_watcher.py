import unittest
from datetime import datetime
from dateutil import relativedelta
import quoter
import inflater
import watcher

class TestWatcher(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(watcher.watch({}), None)

    def test_happy(self):
        res = watcher.watch({
            'NASDAQ:GOOG': { 'upper': 9000, 'lower': 8000 },
            'NASDAQ:FB': { 'lower': 120 },
            'NASDAQ:MSFT': { 'upper': 100 }
            })
        self.assertEqual(len(res), 1)
        self.assertTrue(res['NASDAQ:GOOG']['price'] < 8000)

    def test_unhappy(self):
        res = watcher.watch({'unhappy': None})
        self.assertEqual(res, None)

    def test_none(self):
        res = watcher.watch({
            'NASDAQ:GOOG': {'upper': None, 'lower': 8000},
            'NASDAQ:FB': {'upper': 4, 'lower': None}
            })
        self.assertEqual(len(res), 2)
        self.assertTrue(res['NASDAQ:GOOG']['price'] < 8000)
        self.assertTrue(res['NASDAQ:FB']['price'] > 4)

    def test_sideEffect(self):
        conf = {'NASDAQ:GOOG': {'upper': 90000, 'lower': 1}}
        res = watcher.watch(conf)
        self.assertEqual(res, {})
        self.assertTrue(conf['NASDAQ:GOOG']['price'] > 0)

    def test_inflate(self):
        monthAgo = (datetime.now() - relativedelta.relativedelta(months=1)).strftime('%Y/%m/%d')
        ticker = 'NASDAQ:GOOG'
        quote = quoter.quote([ticker])[ticker]
        inflate = inflater.inflate({'date': monthAgo, 'factor': '15%'})
        res = watcher.watch({
            ticker: { 'lower': quote, 'date': monthAgo, 'factor': '15%'},
            })
        self.assertEqual(len(res), 1)
        self.assertEqual(res[ticker]['inflate'], inflate['inflate'])


if __name__ == '__main__':
    unittest.main()
