# encoding: utf-8
"""
@version:模块导入搜索最大源代码文件
@author:df
"""

import os, pprint, sys

trace = 0 # 1 代表目录 ； 2 代表加上文件

visited = {}
allsize = []

for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        if trace > 0 :
            print(thisDir)

        thisDir = os.path.normpath(thisDir)
        fixcase = os.path.normcase(thisDir)

        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True

        for filename in filesHere:
            if filename.endswith('.py'):
                if trace > 1:
                    print('...', filename)

                pypath = os.path.join(thisDir, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsize.append((pysize, pylines, pypath))

print('By size...')
allsize.sort()
pprint.pprint(allsize[:3])
pprint.pprint(allsize[-3:])

print('By lines...')
allsize.sort(key=lambda x: x[1])
pprint.pprint(allsize[:3])
pprint.pprint(allsize[-3:])
