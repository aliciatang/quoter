import tushare as ts

def quote_tushare(tickers):
    """ (Only for Chinese A shares): Get prices using tushare package and return a dictionary
    of ticker:price as key:value pair. The result may not contain all the given tickers and
    may not return in the same order.

    tickers -- list of tickers, e.g. ['US.MSFT','HK.02186','US.BRK.A', 'US.NSRGY', 'SH.600004','SZ.000651']
    return -- dict of ticker:prices e.g. {'SH.600004': 20,'SZ.000651':41 ...} ignores tickers not valid

    API documents: http://tushare.org/index.html

    """
    if not tickers:
        return {}

    reformated_tickers_SH=[]
    reformated_tickers_SZ=[]
    #putting Shanghai stocks and ShenZhen stocks in two separate lists
    for ticker in tickers:
        if ticker[:2] == 'SH':   #tushare API only works on Chinese A share tickers
            reformated_tickers_SH.append(ticker[3:]) #Getting rid of the exchange codes like 'US' and 'HK'
        elif ticker[:2] == 'SZ':
            reformated_tickers_SZ.append(ticker[3:])
    dict_sh={}
    dict_sz={}
    ret_dict={}

    if reformated_tickers_SH:
        sh=ts.get_realtime_quotes(reformated_tickers_SH)  #sh is pandas dataFrame type
        if sh is not None:
            sh_price=sh['price'].convert_objects(convert_numeric=True) #convert the 'price' column to float and pass it to b
            prefixed_tickers_SH=['SH.'+t for t in sh['code']] #add back deleted exchange code
            dict_sh=dict(zip(prefixed_tickers_SH,sh_price)) #construct {ticker:price} dictionary;
    if reformated_tickers_SZ:
        sz=ts.get_realtime_quotes(reformated_tickers_SZ)
        if sz is not None:
            sz_price=sz['price'].convert_objects(convert_numeric=True)
            prefixed_tickers_SZ=['SZ.'+t for t in sz['code']]
            dict_sz=dict(zip(prefixed_tickers_SZ,sz_price))
    if not dict_sh:
        if not dict_sz:
            print("No valid tickers when getting quotes from tushare API")
        return dict_sz   #if dict_sh is empty,return dict_sz
    else:
        dict_sh.update(dict_sz) #merge two dictionaries into dict_sh
        return dict_sh
'''
tickers=['US.msft','HK.02186','US.BRK.A','US.NSRGY','SH.600004','SH.833330','SZ.000651','US.M0FT','MSFT','SH.510300','SZ.510300','SH.300676','SZ.300676','SZ.833330','SH.833330','SH.600004']
b=quote_tushare(tickers)
print (b)
emptytickers=[]
b=quote_tushare(emptytickers)
print (b)
print('No valid ticker test:')
no_valid_tickers=['US.m0ft']
b=quote_tushare(no_valid_tickers)
print (b)
print('Only SZ test:')
only_sz_tickers=['SZ.000651']
b=quote_tushare(only_sz_tickers)
print(b)
print('Only SH test:')
only_sh_tickers=['SH.600004']
b=quote_tushare(only_sh_tickers)
print(b)
'''

