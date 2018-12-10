# encoding: utf-8
"""
@version:使用quit关闭所有的窗口
@author:df
"""
from tkinter import *
root = Tk()
Button(root, text='pess', command=root.quit).pack(side=LEFT)
root.mainloop()