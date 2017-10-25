from . import iex_data as IEX

def quote_IEX(tickers):
    """ Get prices from IEX APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['US.MSFT','HK.02186','US.BRK.A', 'US.NSRGY', 'SH.600004','SZ.000651']
    return -- dict of ticker:prices e.g. {'US.MSFT': 80,'HK.02186':5.0 ...}

    The iex_data is a python wrapper reference:
        http://www.enlistq.com/python-api-getting-market-financial-data-iex/
        https://github.com/himoacs/iex_data
    The IEX API docs reference:
        https://iextrading.com/developer/docs/#iex-api-1-0
    """
    if not tickers:
        return {}

    reformated_tickers=[]
    for ticker in tickers:
        if ticker[:2] == 'US':
            reformated_tickers.append(ticker[3:]) #Getting rid of the exchange code like 'US' and 'HK'

    reformated_tickers=list(set(reformated_tickers))   #remove duplicate tickers
    iex = IEX.API()
    ret_dict={}
    a=iex.get_latest_trade(reformated_tickers)
    if a is None:
        print('No valid tickers when getting quotes from IEX API')
        return {}
    else:
        ret_dict=a.price.to_dict()
        for key, value in ret_dict.items():
            ret_dict['US.'+key]=ret_dict.pop(key)   #change the key so that the exchange code is added back
        return ret_dict
'''
tickers=['US.msft','HK.02186','US.BRK.A','US.NSRGY','SH.600004','SH.833330','SZ.000651','US.M0FT','MSFT','SH.510300','SZ.510300','SH.300676','SZ.300676','SZ.833330','SH.833330','SH.600004']
b=quote_IEX(tickers)
print(b)
emptytickers=[]
b=quote_IEX(emptytickers)
print(b)
no_valid_tickers=['US.m0ft']
b=quote_IEX(no_valid_tickers)
print(b)
'''
