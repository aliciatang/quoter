#! /usr/local/bin/python3
from quoter import quote

def watch(conf):
    '''
    Watch a list of tickers with upper and lower limit.
    If the current price fall out of either of the limits,
    the ticker will be added to the returned list.

    Side effect alert: the `conf` object passed in will be updated with current market price.

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
        limits['price'] = price
        if 'upper' in limits and limits['upper'] and price >= limits['upper']:
           alerts[ticker] = limits
        if 'lower'in limits and limits['lower'] and price <= limits['lower']:
           alerts[ticker] = limits
    return alerts
