# encoding: utf-8
"""
@version:??
@author:df
"""

import pyttsx3
import pyaudio
import json
import requests
import base64

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
    res = requests.get(host).text
    res = json.loads(res)
    token = res['access_token']
    return token



def baidu_anlay():
    token = get_token()
    audio_data = get_audio()
    audio_data_len = len(audio_data)
    audio_data_bases64 = base64.b64encode(audio_data).decode()

    data = {
        'format':'wav',
        'rate':16000,
        'channel':1,
        'cuid':'asdfasdfasf',
        'token':token,
        'speech':audio_data_bases64,
        'len':audio_data_len,
    }

    data = json.dumps(data).encode()

    url = 'http://vop.baidu.com/server_api'

    header = {'Content-Type':'application/json',}

    req = requests.post(url, headers=header, data=data, verify=False).text

#{"corpus_no":"6634718094253233766","err_msg":"success.","err_no":0,"result":["嗯。"],"sn":"368266649571544765684"}
    res = json.loads(req)['result'][0].replace('。','')

    return res



def test():
    eg = pyttsx3.init()
    eg.say('帅哥')
    eg.runAndWait()

if __name__ == '__main__':

    print(baidu_anlay())