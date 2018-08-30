# encoding: utf-8
"""
@version:??
@author:df
"""

import sys
from threading import Timer
t = Timer(5.5 , lambda: print('Spam!'))
t.start()