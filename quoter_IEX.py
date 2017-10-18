import iex_data as IEX

def quote_IEX(tickers):
    """ Get prices from IEX APIs and return a dictionary of ticker:price as key:value pair.
    The result may not contain all the given tickers and may not return in the same order.

    tickers -- list of tickers, e.g. ['GOOG','MSFT']
    return -- dict of ticker:prices e.g. {'GOOG': 500,'MSFT': 80}
    """
    if not tickers:
        return None
    iex = IEX.API()
    a=iex.get_latest_trade(tickers)
    if a is None:
      return None
    return a.price.to_dict()
