# encoding: utf-8
"""
@version:??
@author:df
"""
import sys

def later():
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')

if __name__ == '__main__':
    later()