from os.path import dirname, basename, isfile
import glob
from .watcher import watch
from .quoter import quote
from .inflater import inflate

__version__ = "0.0.1"

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
