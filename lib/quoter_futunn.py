import futuquant as ft

def quote_futunn(tickers):
    """  Get prices using futuquant API and return a dictionary
    of ticker:price as key:value pair. The API works for US, HK, and Chinese A shares.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','MSFT']
    return -- dict of ticker:prices e.g. {'GOOG': 500,'MSFT': 80}
    API doc: https://futunnopen.github.io/futuquant/intro/intro.html
    """
    if not tickers:
        return None
    quote_ctx=ft.OpenQuoteContext(host="119.29.141.202",port=11111)
    #first step is to subscribe tickers
    sub=quote_ctx.query_subscription()
    subscribed_tickers=[]
    for ticker in tickers:
        ret_code,ret_data = quote_ctx.subscribe(ticker,"QUOTE",push=False)
        if ret_code == -1:
            print("Failed in subscribing ticker:", ticker)
        else:
            subscribed_tickers.append(ticker) #push all successfully subscribed tickers to subscribed_tickers

    sub=quote_ctx.query_subscription()
    print(sub)

    ret_code,ret_data = quote_ctx.get_stock_quote(subscribed_tickers) #get the quote for subscribed tickers
    if ret_code == -1:
        print("Failed getting quotes from futuquant API")
        return None
    price_list=ret_data['last_price'].convert_objects(convert_numeric=True) #convert the 'last_price' column to float and pass it to price_list
    dictionary=dict(zip(subscribed_tickers,price_list)) #construct {ticker:price} dictionary
    if price_list is None:
      return None
    return dictionary
'''
tickers=['SH.600004','SZ.000651','US.AAPL','HK.02186','US.BRKA','US.BRK.A','US.brkb']
b=quote_futunn(tickers)
print (b)
'''
