# encoding: utf-8
"""
@version:??
@author:df
"""

import os, sys, mimetypes, webbrowser

def trace(*args):
    print(*args)


class MediaTool:
    def __init__(self, runtext=''):
        self.runtext = runtext

    def run(self, mediafile, **options):
        fullpath = os.path.join(mediafile)
        self.open(fullpath, **options)

class Filer(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')
        player.write(media.read())

class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile
        os.system(cmdline)

class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT' + mediafile)

class Webbrowser(MediaTool):
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)

audiotools = {
    'sunos5':Filer('/usr/bin/audioplay'),
    'linux2':Cmdline('cat %s > /dev/audio'),
    'sunos4':Filer('/usr/demo/SOUND/play'),
    'win32':Winstart(),
}

wideotools = {
    'linux2':Cmdline('tkcVideo_c700 %s'),
    'win32':Winstart(),
}

imagetools = {
    'linux2':Cmdline('zimager %s'),
    'win32':Winstart(),
}

texttools ={
    'linux2':Cmdline('vi %s'),
    'win32':Cmdline('notepad %s'),
}

apptools = {
    'win32':Winstart(),
}

mimetable = {
    'audio':audiotools,
    'video':videotools,
    'image':imagetools,
    'text':texttools,
    'application':apptools,
}

def trywebbrowser(filename, helpmsg=helpmsg, **options):
    trace('trying browser', filename)
    try:
        player = Webbrowser()
        player.run(filename, **options)
    except:
        print(helpmsg % filename)

def playknownfile(filename, playertable={}, **options):
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrowser(filename, **options)

def playfile(filename, mimetable=mimetable, **options):
    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype == None or encoding is not None:
        contenttype = '?/?'
    maintype, subtype = contenttype.split('/', 1)
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)
    else:
        trywebbrowser(filename, **options)

if __name__ == '__main__':
    playknownfile('sousa.au', audiotools, wait=True)
    playknownfile('ora-pp3e.gif', imagetools, wait=True)
    playknownfile('ora-lp4e.jpg', imagetools)

    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')
    playfile('ora-pp3e.gif')
    playfile('priorcalendar.html')
    playfile('lp4e-preface-preview.html')
    playfile('lp-code-readme.txt')
    playfile('spam.doc')
    playfile('apreadsheet.xls')
    playfile('sousa.au', wait=True)
    input('Done')