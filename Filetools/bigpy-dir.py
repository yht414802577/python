# encoding: utf-8
"""
@version:??
@author:df
"""

import os, glob, sys

dirname = r'F:\1.VIP课后录播视频\8.Django' if len(sys.argv) == 1 else sys.argv[1]

allsize = []
allpy = glob.glob(dirname + os.sep + '*.*')

for filename in allpy:
    filesize = os.path.getsize(filename)
    allsize.append((filesize, filename))

allsize.sort()
print(allsize[:2])
print(allsize[-2:])