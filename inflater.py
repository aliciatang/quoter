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
      'date': '2017/1/1',
      'factor':'2%'
    }
    '''
    if not conf:
        return conf
    today = datetime.datetime.now()
    pattern = re.compile(r'([\d,.+-]*)%')
    if not 'date' in conf or not 'factor' in conf:
        return conf
    try:
        date = parse(conf['date'])
    except:
        return conf
    factors = pattern.findall(conf['factor'])
    if factors:
        factor = locale.atof(factors[0])/100
    if not factor:
        return conf
    days = (today - date).days
    conf['inflate'] = (math.exp(math.log(1 + factor)/356))**days
    return conf
