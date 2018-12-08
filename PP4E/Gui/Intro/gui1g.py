# encoding: utf-8
"""
@version:组件创建后，使用组件的config方法进行组件设置
@author:df
"""

from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world')
widget.pack(side=TOP, expand=YES, fil=BOTH)
root.title('gui1g.py')
root.mainloop()