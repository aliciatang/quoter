from .quoter_IEX import quote_IEX
from .quoter_tushare import quote_tushare
from .quoter_futunn import quote_futunn
from .quoter_alphavantage import quote_alphavantage
from .quoter_yahoo import quote_yahoo
def quote(tickers):
    """ Get prices from several finance APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['US.MSFT','HK.02186','US.BRK.A', 'US.NSRGY', 'SH.600004','SZ.000651']
    return -- dict of ticker:prices e.g. {'US.MSFT': 80,'HK.02186':5.0 ...}

    tickers cannot be quoted will be ignored and printed out
    """
    if not tickers:
        return {}
    tickers = [t.upper() for t in tickers]   #uppercase all tickers
    print(tickers)
    for t in tickers:                        #Output error message when ticker format is wrong
        if t[:3] not in ['US.','HK.','SH.','SZ.']:
            print("Ticker ", t, " is in wrong format!")
    quote_API_list=[quote_yahoo]
    #quote_API_list=[quote_futunn,quote_IEX,quote_tushare,quote_alphavantage]  #the sequence in this list defines which API is used first

    #quote_API_list=[quote_IEX,quote_tushare,quote_alphavantage,quote_futunn]  #the sequence in this list defines which API is used first

    #quote_API_list=[quote_tushare,quote_alphavantage,quote_futunn,quote_IEX]  #the sequence in this list defines which API is used first

    #quote_API_list=[quote_alphavantage,quote_futunn,quote_IEX,quote_tushare]  #the sequence in this list defines which API is used first

    results={}
    remaining_tickers=tickers
    for quote_API in quote_API_list:  #looping through quoters
        try:
            interim_result=quote_API(remaining_tickers)
            if not interim_result:    #if interim_results is None or empty dictionary, continue to next API
                continue
            results.update(interim_result)   #merge interim_result dictionary into results dictionary
            print(remaining_tickers)
            print(interim_result.keys())
            remaining_tickers=[x for x in remaining_tickers if x not in interim_result.keys()] #Remove tickers succesfully quoted each step
            if not remaining_tickers:
                break
        except:
            print("Error in Connecting to", quote_API.__name__)
            continue

    failed_tickers=[x for x in tickers if x not in results.keys()]
    if failed_tickers:
        print('Tickers cannot be quoted: ', failed_tickers)

    return results
'''
tickers=['US.msft','HK.02186','US.BRK.A','US.NSRGY','SH.600004','SH.833330','SZ.000651','US.M0FT','MSFT','SH.510300','SZ.510300','SH.300676','SZ.300676','SZ.833330','SH.833330','SH.600004']
b=quote(tickers)
print (b)
emptytickers=[]
b=quote(emptytickers)
print (b)
print('No valid ticker test:')
no_valid_tickers=['US.m0ft']
b=quote(no_valid_tickers)
print (b)
print('Only SZ test:')
only_sz_tickers=['SZ.000651']
b=quote(only_sz_tickers)
print(b)
print('Only SH test:')
only_sh_tickers=['SH.600004']
b=quote(only_sh_tickers)
print(b)
'''
