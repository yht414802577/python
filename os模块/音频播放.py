# encoding: utf-8
"""
@version:??
@author:df
"""

import pyttsx3

def test():
    eg = pyttsx3.init()
    eg.say('帅哥')
    eg.runAndWait()

if __name__ == '__main__':
    test()