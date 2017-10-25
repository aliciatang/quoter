import futuquant as ft

def quote_futunn(tickers):
    """  Get prices using futuquant API and return a dictionary
    of ticker:price as key:value pair. The API works for US(excluding OTC or pink sheet), HK, and Chinese A shares.
    The result may not contain all the given tickers and may not return in the same order.

    tickers=['SH.600004','SZ.000651','US.AAPL','HK.02186','US.BRK.A']
    This API does not work on OTC stock tickers:['US.NSRGY','US.STVVY']
    return -- dict of ticker:prices e.g. {'US.GOOG': 500,'US.MSFT': 80}
    API doc: https://futunnopen.github.io/futuquant/intro/intro.html
    """
    if not tickers:
        return {}
    quote_ctx = ft.OpenQuoteContext(host = "119.29.141.202", port = 11111)
    #first step is to subscribe tickers
    sub = quote_ctx.query_subscription()
    subscribed_tickers=[]
    for ticker in tickers:
        ret_code, ret_data = quote_ctx.subscribe(ticker, "QUOTE", push = False)
        if ret_code == -1:
            print("Inside futunn API: Failed in subscribing ticker:", ticker)
        else:
            subscribed_tickers.append(ticker) #push all successfully subscribed tickers to subscribed_tickers
    # sub = quote_ctx.query_subscription()  #May check subscription list by this command when debugging
    ret_code , ret_data = quote_ctx.get_stock_quote(subscribed_tickers) #get quotes for subscribed tickers
    if ret_code == -1:
        print("Failed getting quotes from futuquant API")
        return {}
    price_list = ret_data['last_price'].convert_objects(convert_numeric=True) #convert the 'last_price' column to float and pass it to price_list
    if price_list is None:
        print("No valid tickers when getting quotes from futuquant API")
        return {}
    return dict(zip(subscribed_tickers, price_list)) #construct {ticker:price} dictionary

'''
tickers=['US.msft','HK.02186','US.BRK.A','US.NSRGY','SH.600004','SZ.000651','US.M0FT','MSFT','SH.510300','SZ.510300','SH.300676','SZ.300676','SH.833330','SZ.833330','SH.600004']
b=quote_futunn(tickers)
print (b)
emptytickers=[]
b=quote_futunn(emptytickers)
print (b)
no_valid_tickers=['US.m0ft']
b=quote_futunn(no_valid_tickers)
print (b)
'''
