# encoding: utf-8
"""
@version:??
@author:df
"""

from visitor import SearchVisitor

class ReplaceVisitor(SearchVisitor):
    def __init__(self, fromStr, toStr, listOnly=False, trace=0):
        self.change = []
        self.toStr = toStr
        self.listOnly = listOnly
        SearchVisitor.__init__(self, fromStr, trace)

    def visitmatch(self, fromStr, text):
        self.change.append(fname)
        if not self.listOnly:
            fromStr, toStr = self.context, self.toStr
            text = text.replace(fromStr, toStr)
            open(fname, 'w').write(text)

if __name__ == '__main__':
    listOnly = input('List Only') == 'y'
    visitor = ReplaceVisitor(sys.argv[2], sys.argv[3], listOnly)
    if listOnly or input('Proceed whith changes?') == 'y':
        visitor.run(startDir=sys.argv[1])
        action = 'Changed' if not listOnly else 'Found'
        print('Visited %d files' % visitor.fcount)
        print(action, '%d files' % len(visitor.changed))
        for fname in visitor.changed:
            print(fname)