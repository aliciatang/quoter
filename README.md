# Market Quoter
A simple python lib for query stock info from availble free APIs.

## Install:
`pin3 install requests json git+git://github.com/aliciatang/quoter.git@master`

## Usage:
```
python3
>>> from quoter import quote
>>> price = quote(['GOOG', 'NASDAQ: MSFT'])
>>> price
{'NASDAQ:GOOG': 825.89, 'NASDAQ:MSFT': 64.52}
```
