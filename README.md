# Market Quoter
A simple python lib for query stock info from availble free APIs.
Currenly only query google with en_US locale.

## Install:
`pip3 install requests json git+git://github.com/aliciatang/quoter.git@master --upgrade`
add `--upgrade` to get the latest version.

## Usage:
```
python3
>>> from quoter import quote
>>> price = quote(['GOOG', 'NASDAQ: MSFT'])
>>> price
{'NASDAQ:GOOG': 825.89, 'NASDAQ:MSFT': 64.52}
```
