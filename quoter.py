from quoter_IEX import quote_IEX

def quote(tickers):
    """ Get prices from several finance APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','MSFT']
    return -- dict of ticker:prices e.g. {'GOOG': 500,'MSFT': 80}
    """
    if not tickers:
        return None

    result=quote_IEX([t.upper() for t in tickers])
    return result

