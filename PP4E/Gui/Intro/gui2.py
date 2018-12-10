# encoding: utf-8
"""
@version:??
@author:df
"""

from tkinter import *
import sys


widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack()
widget.mainloop()