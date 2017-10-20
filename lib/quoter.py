from quoter_IEX import quote_IEX
from quoter_tushare import quote_tushare
def quote(tickers):
    """ Get prices from several finance APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','MSFT']
    return -- dict of ticker:prices e.g. {'GOOG': 500,'MSFT': 80}
    """
    if not tickers:
        return None
    tickers = [t.upper() for t in tickers]
    us_tickers = []
    cn_tickers = []
    hk_tickers = []
    for t in tickers:
        if t.isdigit():
            if len(t) == 6:
                cn_tickers.append(t)
            elif len(t) == 4:
                hk_tickers.append(t)
        else:
            us_tickers.append(t)
    print(us_tickers,'and',cn_tickers,'and',hk_tickers)

    if us_tickers:
       us_result = quote_IEX(us_tickers)
    else: us_result={'None':0}
    if cn_tickers:
       cn_result = quote_tushare(cn_tickers)
    else: cn_result={}
    if hk_tickers:
       hk_result = quote_tushare(hk_tickers)
    else: hk_result={}
    print(cn_result)
    ## merge cn_resutls and us_result
    results=us_result
    results.update(cn_result)
    print(results)
    results.update(hk_result)
    print(results)
    return results
'''
tickers=['600004','msft']
results=quote(tickers)
print(results)
'''
