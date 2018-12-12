# encoding: utf-8
"""
@version:??
@author:df
"""

from tkinter import *
import sys
class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method world')
        sys.exit()

HelloClass()
mainloop()