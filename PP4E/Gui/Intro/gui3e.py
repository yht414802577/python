# encoding: utf-8
"""
@version:鼠标左键双击或者单击
@author:df
"""

import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')

def quit(event):
    print('Hello, I must be going ...')
    sys.exit()

widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)  #鼠标单击左键
widget.bind('<Double-1>', quit)   #鼠标双击左键
widget.mainloop()