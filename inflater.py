#! /usr/local/bin/python3
import datetime, re, locale, math
from dateutil.parser import parse
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def inflate(conf):
    '''
    Infate the upper and lower limit in config with inflation factor.

    Side effect alert: the time and inflation factor will be removed form the `conf` object.

    Example conf:
    {
      'NASDAQ:GOOG': { 'upper': 900, 'lower': 432, 'date': '2017/1/1', 'factor':'2%'},
      'NASDAQ:FB': { 'lower': 120, 'date': '2017/2/2', 'factor':'10%'},
      'NASDAQ:MSFT': { 'upper': 100, }
    }
    '''
    today = datetime.datetime.now()
    pattern = re.compile(r'([\d,.+-]*)%')
    for ticker, cfg in conf.items():
        if 'date' in cfg and 'factor' in cfg:
            try:
                date = parse(cfg['date'])
            except:
                date = None
            factors = pattern.findall(cfg['factor'])
            if factors:
                factor = locale.atof(factors[0])/100
            if date and factor:
                days = (today - date).days
                cfg['inflate'] = (math.exp(math.log(1 + factor)/356))**days
    return conf
