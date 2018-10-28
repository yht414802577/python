# encoding: utf-8
"""
@version:??
@author:df
"""

import os, sys
from Tools import find

count = 0

for filename in find.find('.pyc', sys.argv[1]):
    count += 1
    print(filename)
    os.remove(filename)

print('Removed %d .pyc files' % count)