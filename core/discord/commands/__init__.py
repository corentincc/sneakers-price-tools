from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
for f in modules:
    if isfile(f) and not f.endswith("__init__.py"):
        exec(f"from . import {basename(f)[:-3] }")
