# encoding: utf-8
"""
@version:??
@author:df
"""

import os, sys

class FileVisitor:
    """
    访问startDir（默认为'.）下所有非目录文件，可通过重载visit*方法定制文件/目录处理器；情境参数/属性为可选的子类特异的状态；
    追踪开光：0代表关闭、1代表显示目录、2代表显示目录及文件
    """
    def __init__(self, cobtext=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.conttext = conttext
        self.trace = trace

    def run(self, startDir=os.curdir, reset=True):
        if reset:
            self.reset()
        for (thisDir, dirsHere, filesHere) in os.walk(startDir):
            self.visitdir(thisDir)
            for fname in filesHere:
                fpath = os.path.join(thisDir, fname)
                self.visitfile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        self.dcount += 1
        if self.trace > 0:
            print(dirpath, '...')

    def visitfile(self, filepath):
        self.fcount += 1
        if self.trace > 1:
            print(self.fcount, '=>', filepath)

class SearchVisitor(FileVisitor):
    """
    在startDir及其子目录下的文件中搜索字符串；
    子类：根据需要重新定义visitmatch，扩展列表和候选；
    子类可以使用testexts来指定进行搜索的文件类型（还可以重定义候选以对文本内容使用mimetypes：参考之前相关部分
    """
    shipexts = []
    testexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']

    def __init__(self, searchkey, trace=2):
        FileVisitor.__init__(self, searchkey, trace)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.testexts:
            return ext in self.testexts
        else:
            return ext not in self.skipexts

    def visitfile(self, fname):
        FileVisitor.visitfile(self, fname)
        if not self.candidate(fname):
            if self.trace > 0:
                print('Skipping', fname)
        else:
            text = open(fname).read()
            if self.context in text:
                self.visitmatch(fname, text)
                self.scount += 1
                print('%s has %s' %(fname, self.context))

if __name__ == '__main__':
    dolist = 1
    dosearch = 2
    donext = 4

    def selftest(testmask):
        if testmask & dolit:
            vistor = FileVisitor(trace=2)
            vistor.run(sys.argv[2])
            print('Visited %d files and %d dirs' %(visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace=0)
            visitor.run(sys.argv[2])
            print('Found in %d files, visited %d' %(vistor.scount, visitor.fcount))
    selftest(int(sys.argv[1]))
