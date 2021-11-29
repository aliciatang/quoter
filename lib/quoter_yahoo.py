import yfinance as yf


"""
Yahoo finance country/exchange code. For US stock,there is no prefix.
for SH prefix need to be changed to '.SS' surfix.
for SZ prefix need to be changed to '.SZ' surfix.
"""
def quote_yahoo(tickers):
    """ Get prices from yahoo finance APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['US.MSFT','HK.02186','US.BRK.A', 'US.NSRGY', 'SH.600004','SZ.000651']
    return -- dict of ticker:prices e.g. {'US.MSFT': 80,'HK.02186':5.0 ...}

    The yfinance is a python wrapper reference:
        https://github.com/ranaroussi/yfinance
    """
    if not tickers:
        return {}

    reformated_tickers=[]
    for ticker in tickers:
        if ticker[:3] == 'US.': # has country code since the 3rd charactor is '.'
            formated_ticker = ticker[3:] #Getting rid of the country code like 'US' and 'HK'
            formated_ticker = formated_ticker.replace('.', '-', 1) # change BRK.A -> BRK-A to meet yahoo ticker syntax
            reformated_tickers.append(formated_ticker)
        elif ticker[:3] == 'SH.':
            formated_ticker = ticker[3:] + '.SS'
            reformated_tickers.append(formated_ticker)
        elif ticker[:3] == 'SZ.':
            formated_ticker = ticker[3:] + '.SZ'
            reformated_tickers.append(formated_ticker)
        else:
            print('matched none')

    if(len(reformated_tickers) == 1):
        reformated_tickers.append('GOOG') # appending GOOG to make sure there is at least two tickers.
    reformated_tickers=list(set(reformated_tickers))   #remove duplicate tickers
    ret_dict={}
    tickers = yf.Tickers(reformated_tickers)
    if not tickers.tickers:
        print('No valid tickers when getting quotes from yahoo finance API')
        return {}
    else:
        hist = tickers.history(period="1d")
        for tick in tickers.tickers:
            if tick[-3] == '.SS':
                restored_ticker = 'SH.' + ticker[:-3]
            elif tick[-3] == '.SZ':
                restored_ticker = 'SZ.' + ticker[:-3]
            else:
                restored_ticker = 'US.' +tick.replace('-','.')
            ret_dict[restored_ticker]=hist['Close'][tick][0]
        return ret_dict
'''
tickers=['US.msft','HK.02186','US.BRK.A','US.NSRGY','SH.600004','SH.833330','SZ.000651','US.M0FT','MSFT','SH.510300','SZ.510300','SH.300676','SZ.300676','SZ.833330','SH.833330','SH.600004']
b=quote_yahoo(tickers)
print(b)
emptytickers=[]
b=quote_yahoo(emptytickers)
print(b)
no_valid_tickers=['US.m0ft']
b=quote_yahoo(no_valid_tickers)
print(b)
'''
