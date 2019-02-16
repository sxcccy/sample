#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'jiang'
import eyed3
import wave
import os
import speech_recognition as sr
from pydub import AudioSegment
import time
import datetime

#更改当前目录
os.chdir(r'D:\Documents\Videos')
#要处理的文件
file1=r'The Basics of Affiliate MarketingG_P@FB.wav'
dir1=file1[0:len(file1)-4]
os.makedirs(dir1)
with open("D:\google cloud\My First Project-26836f62ed30.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
# ##获取音频时长
f = wave.open(file1,"rb")
timelength=int(f.getparams()[3]/f.getparams()[2])
print(timelength)
#
# ##音频分割输出
readaudio=AudioSegment.from_wav(file1)
kn=int(timelength/30)+1
for i in range(kn):
    readaudio[i*30*1000:((i+1)*30+2)*1000].export(dir1+'\\%08d.wav'%(i+1), format="wav")
##获取文件夹下的音频文件名
starttime = datetime.datetime.now()
for name in os.listdir(dir1):
    print("%s 开始转换" % (name))
    ##音频分块识别
    r = sr.Recognizer()
    
    try:
        with sr.WavFile(dir1+'\\%s' % name) as source:
            audio = r.record(source)
            text=( r.recognize_google_cloud(audio,credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS,language='en-US')+'\n')
            open(dir1+r'.txt', 'a+').write('\n'+text)
            
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %s 已完成' % (temptime, name))

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %s 未完成' % (temptime, name))
        continue

jietime = datetime.datetime.now()
last=jietime-starttime
print('总共花费时间：%s'%last)
