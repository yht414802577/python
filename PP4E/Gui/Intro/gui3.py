# encoding: utf-8
"""
@version:回调函数
@author:df
"""

from tkinter import *
import sys

def quit():
    print('Hello, I must bu going')
    sys.exit()

widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()