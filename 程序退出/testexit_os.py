# encoding: utf-8
"""
@version:??
@author:df
"""

import os

def outahere():
    print('Bye os world')
    os._exit(99)
    print('word reached')

if __name__ == '__main__':
    outahere()