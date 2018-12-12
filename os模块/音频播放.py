# encoding: utf-8
"""
@version:??
@author:df
"""

import pyttsx3
import pyaudio
import json
import requests

def get_audio():
    pa = pyaudio.PyAudio()
    audio_reuqui = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1023,
    )
    times = 0
    data = []

    while times < 45:
        audio_data = audio_reuqui.read(1024)
        data.append(audio_data)
        times += 1

    audio_reuqui.close()
    res = b''.join(data)
    return res

def get_token():
    url = ' https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
    client_id = 'xq4LTn8xQTKml4vnmY4NNtpG'
    client_secret = 'B9KcshnGDPjTjqyWgWyScdMmnm8zAQD7'
    host = url % (client_id, client_secret)
    res = requests.get(host).text.decode()



def baidu_anlay(get_audio):
    data = {
        'format':'wav,'
        'rate':16000,
        'channel':1,
        'cuid':'asdfasdfasf',
        'token':
    }



def test():
    eg = pyttsx3.init()
    eg.say('帅哥')
    eg.runAndWait()

if __name__ == '__main__':
    test()
    print(get_audio())