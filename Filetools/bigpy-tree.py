# encoding: utf-8
"""
@version:找出整个目录树中最大的python源代码文件。搜索文件，利用pprint漂亮的显示结果
@author:df
"""

import sys, os, pprint

trace = False

if sys.platform.startswith('win'):
    dirname = r'F:\1.VIP课后录播视频'
else:
    dirname = '/usr/lib/python'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace:
        print(thisDir)

    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])