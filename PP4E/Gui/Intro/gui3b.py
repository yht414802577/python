# encoding: utf-8
"""
@version:??
@author:df
"""

from tkinter import *
import sys

widget = Button(None, text='Hello event world', command=(lambda: print('Hello lambda world') or sys.exit()))
widget.pack()
widget.mainloop()