#!/usr/bin/env python   
# -*- coding: UTF-8 -*-

import base64


jiemi= 'eyJuaWNrbmFtZSI6IuadqOa1t-a2myIsInNoYXJlR29vZHNUeXBlIjoiIiwic2hhcmVVc2VySWQiOiJkNDUxMDRmM2QzZWY0ZTJkOTM5YzEyZTM0YjVlOTRmZCIsInRpdGxlIjoiIOW_lyDmhL8g6ICFIOWVhiDln44gIiwidGV4dCI6IuWOn-S6p-WcsOeyvuaMkee7humAiembtuW3ruS7t-i2heWAvOS8mOaDoO-8jOi1tuW_q-adpeeci-eci-WQp-OAgiIsInNoYXJlUGFnZSI6Im1lbWJlck1hbGwifQ'
data = base64.b64decode(jiemi)
print data
