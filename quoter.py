import requests,json

def quote(tickers):
    """ Get prices from google finace and return a list of object with
    exchange:ticker as the key, and price as the value. The result may
    not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','NASDAQ:MSFT']
    return -- list of prices e.g. [{'NASDAQ:GOOG': 500},{'NASDAQ:MSFT': 80}]
    """
    if not tickers:
        return None

    baseUrl = 'http://finance.google.com/finance/info?q='
    url = baseUrl + ",".join(tickers)
    response = requests.get(url)
    response.connection.close()
    if response.status_code != 200 :
        return None

    data = json.loads(response.text.replace('//', ''))
    result = {}
    for item in data:
        result[item['e']+":"+item['t']] = float(item['l'])
    return result

