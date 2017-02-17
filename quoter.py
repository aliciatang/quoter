import requests,json

def getPrices(tickers):
    """ Get prices from google finace and return a list of object with
    exchange:ticker as the key, and price as the value. The result may
    not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','NASDAQ:MSFT']
    return -- list of prices e.g. [{'NASDAQ:GOOG': 500},{'NASDAQ:MSFT': 80}]
    """
    baseUrl = 'http://finance.google.com/finance/info?q='
    url = baseUrl + ",".join(tickers)
    response = requests.get(url)
    data = json.loads(response.text.replace('//', ''))
    result = {}
    for item in data:
        result[item['e']+":"+item['t']] = item['l']
    return result

prices = getPrices(['NASDAQ:GOOG','NASDAQ:MSFT'])

