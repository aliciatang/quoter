from setuptools import setup, find_packages

setup(name = 'quoter',
      version = '0.0.2',
      description = 'Quote stock price by ticker',
      author = 'Alicia Tang',
      author_email = 'alicia.x.tang@gmail.com',
      url = 'https://github.com/aliciatang/quoter',
      package_dir={'quoter': 'lib'},
      packages=['quoter'],
      install_requires=[package.split("\n")[0] for package in open("requirements.txt", "r").readlines()]
     )
