import tushare as ts

def quote_tushare(tickers):
    """ (Only for Chinese A shares: Get prices using tushare package and return a dictionary
    of ticker:price as key:value pair. The result may not contain all the given tickers and
    may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','MSFT']
    return -- dict of ticker:prices e.g. {'GOOG': 500,'MSFT': 80}
    """
    if not tickers:
        return None
    a=ts.get_realtime_quotes(tickers)  #a is pandas dataFrame type
    b=a['price'].convert_objects(convert_numeric=True) #convert the 'price' column to float and pass it to b
    dictionary=dict(zip(tickers,b)) #construct {ticker:price} dictionary
    if a is None:
      return None
    return dictionary
'''
tickers=['600004','000651']
b=quote_tushare(tickers)
print (b)
'''
