from alpha_vantage.timeseries import TimeSeries

def quote_alphavantage(tickers):
    """ Get prices from alpha vantage API and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['US.MSFT','HK.02186','US.BRK.A', 'US.NSRGY', 'SH.600004','SZ.000651']
    return -- dict of ticker:prices e.g. {'US.MSFT': 80,'HK.02186':5.0 ...}

    API documents: https://www.alphavantage.co/documentation/#
    Wrapper documents: https://github.com/RomelTorres/alpha_vantage
    """
    if not tickers:
        return {}
    reformated_tickers=[]
    for ticker in tickers:
        if ticker[:2] == 'US':
            reformated_tickers.append(ticker[3:]) #Getting rid of the exchange code like 'US' and 'HK'
    reformated_tickers=list(set(reformated_tickers))   #remove duplicate tickers
    ts = TimeSeries(key='O9MJAB5GUVPP5Z38',output_format='pandas')
    ret_dict={}
    for ticker in reformated_tickers:
        try:
            data,meta_data = ts.get_intraday(symbol=ticker,interval='1min')
            ret_dict['US.'+ticker]=data['close'][-1]  #add the latest price of ticker to ret_dict,add back exchange code 'US.'
        except ValueError:
            print('Inside AlphaVantage API: ticker', ticker, 'is not valid')
            continue        #if ticker is not valid, try the next ticker, until tickers list is exhausted

    if not ret_dict:
        print("No valid tickers when getting quotes from Alpha Vantage API")
    return ret_dict

'''
tickers=['US.msft','HK.02186','US.BRK.A','US.MSFT','US.NSRGY','SH.600004','SZ.000651','US.M0FT','MSFT']
b=quote_alphavantage(tickers)
print(b)
emptytickers=[]
b=quote_alphavantage(emptytickers)
print(b)
no_valid_tickers=['US.m0ft']
b=quote_alphavantage(no_valid_tickers)
print(b)
'''
