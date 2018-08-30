# encoding: utf-8
"""
@version:??
@author:df
"""

from tkinter import Tk
from tkinter.messagebox import showinfo
win = Tk()
win.after(5500, lambda: showinfo('Popup', 'Spam!'))

win.after(5500, showinfo, 'Popup', 'Spam')