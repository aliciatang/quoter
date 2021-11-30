#! /usr/local/bin/python3
from .quoter import quote
from .inflater import inflate
from itertools import groupby

def watch(conf):
    '''
    Watch a list of tickers with upper and lower limit.
    If the current price fall out of either of the limits,
    the ticker will be added to the returned list.

    Side effect alert: the `conf` object passed in will be updated with current market price.

    Example conf:
    {
      'US.GOOG': { 'upper': 900, 'lower': 432 ,'date': '2017/1/1', 'factor': '5%'},
      'US.FB': { 'lower': 120 },
      'US.MSFT': { 'upper': 100}
    }
    '''
    # partition keys by prefix
    keys = list(conf.keys())
    keys.sort()
    prices = {}
    for key, group in groupby(keys, lambda x: x[:3]):
        parts = []
        for thing in group:
            parts.append(thing)
        prices.update(quote(parts))

    alerts = {}
    for ticker, price in prices.items():
        limits = inflate(conf[ticker])
        limits['price'] = price
        if 'inflate' in limits and limits['inflate']:
            price = price/limits['inflate']
            if 'upper' in limits and limits['upper']:
                limits['adjUpper'] = limits['upper'] * limits['inflate']
            if 'lower' in limits and limits['lower']:
                limits['adjLower'] = limits['lower'] * limits['inflate']

        if 'upper' in limits and limits['upper'] and price >= limits['upper']:
           alerts[ticker] = limits
        if 'lower'in limits and limits['lower'] and price <= limits['lower']:
           alerts[ticker] = limits
    return alerts
