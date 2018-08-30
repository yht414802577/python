# encoding: utf-8
"""
@version:??
@author:df
"""

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('47.104.224.67',23334))
while True:
    msg = input('qingshuo')
    if msg == 'exit':
        break
    s.send(msg.encode('utf-8'))
    date = s.recv(1024)
    print(date.encode(utf-8))



