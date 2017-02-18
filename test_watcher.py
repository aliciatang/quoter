import unittest
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
        self.assertTrue('NASDAQ:GOOG' in res)
        self.assertTrue(res['NASDAQ:GOOG']['price'] < 8000)

    def test_unhappy(self):
        res = watcher.watch({'unhappy': None})
        self.assertEqual(res, None)

if __name__ == '__main__':
    unittest.main()
