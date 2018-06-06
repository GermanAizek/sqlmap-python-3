#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import sys

PYVERSION = sys.version.split()[0]

if PYVERSION < "3":
    exit("[CRITICAL] incompatible Python version detected ('%s'). To successfully run sqlmap you'll have to use version 3.6.x (visit 'https://www.python.org/downloads/')" % PYVERSION)

extensions = ("bz2", "gzip", "ssl", "sqlite3", "zlib")
try:
    for _ in extensions:
        __import__(_)
except ImportError:
    errMsg = "missing one or more core extensions (%s) " % (", ".join("'%s'" % _ for _ in extensions))
    errMsg += "most likely because current version of Python has been "
    errMsg += "built without appropriate dev packages (e.g. 'libsqlite3-dev')"
    exit(errMsg)
