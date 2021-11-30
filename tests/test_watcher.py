import unittest
from datetime import datetime
from dateutil import relativedelta
from lib import quoter
from lib import inflater
from lib import watcher

class TestWatcher(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(watcher.watch({}), {})

    def test_happy(self):
        res = watcher.watch({
            'US.GOOG': { 'upper': 9000, 'lower': 8000 },
            'US.FB': { 'lower': 120 },
            'US.MSFT': { 'upper': 100 }
            })
        self.assertTrue(res['US.GOOG']['price'] < 8000)

    def test_unhappy(self):
        res = watcher.watch({'unhappy': None})
        self.assertEqual(res, {})

    def test_none(self):
        res = watcher.watch({
            'US.GOOG': {'upper': None, 'lower': 8000},
            'US.FB': {'upper': 4, 'lower': None}
            })
        self.assertEqual(len(res), 2)
        self.assertTrue(res['US.GOOG']['price'] < 8000)
        self.assertTrue(res['US.FB']['price'] > 4)

    def test_sideEffect(self):
        conf = {'US.GOOG': {'upper': 90000, 'lower': 1}}
        res = watcher.watch(conf)
        self.assertEqual(res, {})
        self.assertTrue(conf['US.GOOG']['price'] > 0)

    def test_inflate(self):
        monthAgo = datetime.now() - relativedelta.relativedelta(months=1)
        ticker = 'US.GOOG'
        quote = quoter.quote([ticker])[ticker]
        inflate = inflater.inflate({'date': monthAgo, 'factor': 0.18})
        res = watcher.watch({
            ticker: { 'lower': quote, 'upper': quote* 1.8, 'date': monthAgo, 'factor': 0.18},
            })
        self.assertEqual(len(res), 1)
        self.assertEqual(res[ticker]['inflate'], inflate['inflate'])
        self.assertTrue(res[ticker]['adjLower'] > res[ticker]['lower'])
        self.assertTrue(res[ticker]['adjUpper'] > res[ticker]['upper'])

    def test_inflateNone(self):
        monthAgo = datetime.now() - relativedelta.relativedelta(months=1)
        ticker = 'US.GOOG'
        quote = quoter.quote([ticker,'US.MSFT'])[ticker]
        print(quote)
        inflate = inflater.inflate({'date': monthAgo, 'factor': 0.18})
        print(inflate)
        conf = { ticker: { 'lower': None, 'upper': None, 'date': monthAgo, 'factor': 0.18},
                 }
        res = watcher.watch(conf)
        self.assertEqual(conf[ticker]['inflate'], inflate['inflate'])
        self.assertFalse('adjLower' in conf[ticker])
        self.assertFalse('adjUpper' in conf[ticker])

    def test_partition(self):
        conf={'SH.600004':{},'SH.600276':{}, 'US.GOOG':{}}
        res = watcher.watch(conf)
        self.assertTrue(conf['SH.600004']['price'] > 0)
        self.assertTrue(conf['SH.600276']['price'] > 0)
        self.assertTrue(conf['US.GOOG']['price'] > 0)


if __name__ == '__main__':
    unittest.main()
