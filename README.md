# Market Quoter
A simple python lib for query stock info from availble free APIs.
Currenly only using yahoo with en_US locale by default.
This support US, HK and China stock markets. 

## Install:
`pip3 install git+git://github.com/aliciatang/quoter.git@master --upgrade`
add `--upgrade` to get the latest version.

## Usage:
```
python3
>>> from quoter import quote
>>> price = quote(['US.GOOG', 'US.MSFT'])
>>> price
{'US.GOOG': 825.89, 'US.MSFT': 64.52}
```
For international stocks use the following prefix.
```python3
US -> US
HK -> HongKong
SH -> Shang Hai
SZ -> Shen Zhen
```

## Tests:

* run single test
```
python3 -m tests.test_quoter TestGetPrices.test_HK
```

* run all tests
```
python3 -m tests.test_quoter
```
