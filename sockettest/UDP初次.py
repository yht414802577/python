# encoding: utf-8
"""
@version:??
@author:df
"""

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:

    for i in range(100):
        date1 = 'hahahahahaah'
        s.sendto(date1.encode('utf-8'),('47.104.224.67',25556))

    date,c_addr = s.recvfrom(1024)
    print(date.decode('utf-8'))
