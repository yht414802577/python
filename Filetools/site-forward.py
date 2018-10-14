# encoding: utf-8
"""
@version:??
@author:df
"""

import os

servername = 'learning-python.com'
homedir = 'books'
sitefilesdir = r'E:\PycharmProjects\python\aaa\templates'
uploaddir = r'E:\PycharmProjects\python\first\tempppp\html'
templatename = 'template.html'

try:
    os.mkdir(uploaddir)
except OSError:
    pass

template = open(templatename).read()
sitefiles = os.listdir(sitefilesdir)

count = 0

for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = os.path.join(uploaddir, filename)
        print('creating', filename, 'as', fwdname)
        filetext = template.replace('$server$', servername)
        filetext = filetext.replace('$home$',homedir)
        filetext = filetext.replace('$file$',filename)
        open(fwdname, 'w').write(filetext)
        count += 1

print('Last file => \n', filetext, sep='')
print('Done:', count, 'forward files created.')
