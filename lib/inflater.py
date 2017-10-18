#! /usr/local/bin/python3
import datetime, math

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
    if not 'date' in conf or not 'factor' in conf:
        return conf
    date = conf['date']
    factor = conf['factor']
    if not date or not factor:
        return conf
    days = (today - date).days
    conf['inflate'] = (1 + (factor/365))**days
    return conf
