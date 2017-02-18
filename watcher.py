#! /usr/local/bin/python3
from quoter import quote

def watch(conf):
    '''
    Watch a list of tickers with upper and lower limit.
    If the current price fall out of either of the limits,
    the ticker will be added to the returned list.

    Example conf:
    {
      'NASDAQ:GOOG': { 'upper': 900, 'lower': 432 },
      'NASDAQ:FB': { 'lower': 120 },
      'NASDAQ:MSFT': { 'upper': 100}
    }
    '''
    prices = quote(list(conf.keys()))
    if not prices:
        return None
    alerts = {}
    for ticker, price in prices.items():
        limits = conf[ticker]
        if 'upper' in limits and price >= limits['upper']:
           alerts[ticker] = limits
           alerts[ticker]['price'] = price
        if 'lower'in limits and price <= limits['lower']:
           alerts[ticker] = limits
           alerts[ticker]['price'] = price
    return alerts
