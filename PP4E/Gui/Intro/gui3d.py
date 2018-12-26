# encoding: utf-8
"""
@version:启动__call__方法处理tkinter内部的调用
@author:df
"""

import sys
from tkinter import *

class HelloCallable:
    def __init__(self):
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)
        sys.exit()

widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()