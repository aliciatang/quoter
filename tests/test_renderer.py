import unittest
import datetime
from dateutil import relativedelta
from lib import renderer

class TestRenderer(unittest.TestCase):

    def test_empty(self):
        alerts = {'US.ADSK': {'adjLower': 277.1943867166462, 'date': datetime.datetime(2020, 8, 30, 0, 0), 'factor': 0.24, 'inflate': 1.3521677400812009, 'lower': 205.0, 'memo': '', 'price': 257.6600036621094, 'upper': None}}
        html = renderer.render(alerts)
        self.assertEqual(html, "<html><body><ul><li>US.ADSK($257.6600036621094) falls below adjusted limit($277.1943867166462 with factor:24.00%)</li></body></ul></html>")



if __name__ == '__main__':
    unittest.main()
