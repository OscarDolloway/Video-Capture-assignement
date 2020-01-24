#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:13:57 2019

@author: oscardolloway
"""


from __future__ import print_function
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys
import matplotlib.image as mpimg
from matplotlib.pyplot import figure, imshow, axis
import cv2
import ffmpeg
import sys
import subprocess as sp
from threading import Timer
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
import sys
import numpy as np
import re
count = 1
getsites = []


FFMPEG_BIN ='/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/ffmpeglib/bin/ffmpeg'

path1 = '/Users/oscardolloway/Documents/GitHub/LogoDetection/Logos/'

files = os.listdir(path1)
#cascPath = sys.argv[1]
face_cascade = cv2.CascadeClassifier('/Users/oscardolloway/Documents/GitHub/LogoDetection/haarcascade_frontalface_default.xml')
Video = '/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/jelly.mp4'

#video_capture = cv2.VideoCapture(0)

m3u8URL = 'http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8'
m3u8_URL = 'http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'

# =============================================================================
# Reads the MP4 file, small issue regarding the way Macs read videos
# =============================================================================
def mp4capture():
    if (video_capture.isOpened()==False):
        print("Error opening video")
        
    while True:
        ret, frame = video_capture.read()
        fshape = frame.shape
        height= fshape[0]
        width = fshape[1]
    
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('webcamsave.mp4',fourcc,24,(width,height))
        #print(fshape[0],fshape[1])
        #height = fshape[0]
        #grayvid = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(frame, 1.1, 5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)#change scale factor to 1.2/1.3 if not recognising all faces 
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        out.write(frame)
        cv2.imshow('MP4', frame)
        
        #cv2.show()
        
        key = cv2.waitKey(1) & 0xFF
        if key ==  ord('q'):
            break
        
    
    video_capture.release()
    cv2.destroyAllWindows()

#mp4capture()



def m3u8capture():
    command = [FFMPEG_BIN,'-i',Video
               ,
               '-ss','1','-f','image2pipe',
               '-pix_fmt','rgb24',
               '-vcodec','rawvideo',
               '-']
    
    #infocommand = [FFMPEG_BIN,'-i',Video,'-']
# =============================================================================
#     pipe gets video information ()
# =============================================================================
    pipe = sp.Popen(command, stdout = sp.PIPE,bufsize=10**8)
    
    
    raw_image = pipe.stdout.read(420*360*3)
    image = np.fromstring(raw_image,dtype='uint8')
    image = image.reshape((360,420,3))
    plt.imshow(image)
    plt.show()
    pipe.stdout.flush()
    
#m3u8capture()
    
# =============================================================================
# working but not showing correct video
# =============================================================================
def live_cap():
    
    VIDEO_URL = m3u8URL
    pipe = sp.Popen([ FFMPEG_BIN, "-i", VIDEO_URL,
            # no text output
               # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-r",'1',
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)
    while True:
        raw_image = pipe.stdout.read(1920*1080*3) # read 432*240*3 bytes (= 1 frame)
        image =  np.frombuffer(raw_image, dtype='uint8').reshape((1080,1920,3))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('webcamsave.mp4',fourcc,24,(1920,1080))
        cv2.imshow("m3u8",image)
        out.write(image)
        key = cv2.waitKey(1) & 0xFF
        if key ==  ord('q'):
            break
        
        cv2.destroyAllWindows()
    
#live_cap()

def vidconvert(video_input, video_output):
    cmds = [FFMPEG_BIN,'-i',video_input,video_output]
    sp.run(cmds)
# =============================================================================
#     print(cmds)
# =============================================================================
    
#vidconvert('jelly.mp4','jelly.mov')

def m3u8test():
    
    VIDEO_URL = m3u8URL
    
    cap=cv2.VideoCapture(VIDEO_URL)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    current_frame = 0
    
# =============================================================================
#     get video data
# =============================================================================
    while (True):
        ret, frame = cap.read()
        #print(frame)
        #fshape = frame.shape
        #height= fshape[0]
        #width = fshape[1]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('live.mp4',fourcc,24,(int(width),int(height)))
        #frame = cv2.flip(frame,current_frame)
        print(current_frame)
        a = cv2.imshow("video", frame)
        
        out.write(cv2.flip(frame, 180))
        if (ret != True):
            break
        
        

        if cv2.waitKey(25)== 27:
            break
        
        current_frame +=1
        
#m3u8test()

def Time ():
    
    t = Timer(60.0, time)
    
    if t == 60.0:
        t.cancel()
    
def storingtest1():
    
    VIDEO_URL = m3u8URL

    cap=cv2.VideoCapture(VIDEO_URL)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('live.mp4',fourcc,24,(int(width),int(height)))
    current_frame = 0
    
    a_count = 0
    
    while (cap.isOpened()):
        
        ret, frame = cap.read()
        a_count = a_count + 1
        
        if ret == True:
            
            #frame = cv2.flip(frame,current_frame)
        #print(frame)
        #fshape = frame.shape
        #height= fshape[0]
        #width = fshape[1]
        
        #frame = cv2.flip(frame,current_frame)
            #print(current_frame)
           
            a = cv2.imshow("video", frame)
            out.write(cv2.flip(frame, 180))
            #print(out.get(cv2.CAP_PROP_POS_MSEC))
        else:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        #print(out.get(cv2.CAP_PROP_POS_MSEC))
        current_frame +=1
    print('a',a_count)
    cap.release()
    out.release()
    cv2.destroyAllWindows()
        
        
# =============================================================================
#storingtest1()
# =============================================================================


def beginnerscraper():
    url = "http://xmtvplayer.com/snippet/sample-m3u-file"
    #content = global
    site = urlopen(url).read()

    #print(site)
    #for i in content:
        #print(i)
    soup = BeautifulSoup(site,features="lxml",)
    content = soup.find_all("p", {"class": "box"},"")
    b = soup.find_all("p")
    #sitelist = [str(b)]
    #print(sitelist)
    sitelist = b.text
    links = re.findall("(?P<element>(https?)[\w\.\/\-\\:]+)",sitelist)#insert regex
    x = re.search("p(?P<element>[\d]+)",All)
    
    
    
    #print (soup.prettify())
    #print (title)

beginnerscraper()
