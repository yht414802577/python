# encoding: utf-8
"""
@version:通过继承来设定组件
@author:df
"""

from tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()

if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()