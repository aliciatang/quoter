from distutils.core import setup

setup(name = 'quoter',
      version = '0.0.1',
      description = 'Quote stock price by ticker',
      author = 'Alicia Tang',
      author_email = 'alicia.x.tang@gmail.com',
      url = 'https://github.com/aliciatang/quoter',
      py_modules = ['lib.quoter', 'lib.watcher', 'lib.inflater'],
     )
