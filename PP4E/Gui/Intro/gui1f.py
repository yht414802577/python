# encoding: utf-8
"""
@version:text选项在标签创建后进行设置，向组件指定文本关键字。————————选项也可以像字典一样
@author:df
"""

from tkinter import *

widget = Label()
widget['text'] = 'Hello GUI world'
widget.pack(side=TOP)
mainloop()