#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:13:57 2019

@author: oscardolloway
"""

from __future__ import print_function

import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.image as mpimg
from matplotlib.pyplot import figure, imshow, axis
import cv2
import sys
import subprocess as sp
from threading import Timer
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import re
import requests
    
count = 1
getsites = []


FFMPEG_BIN ='/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/ffmpeglib/bin/ffmpeg'
ffprobe = '/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/ffmpeglib/bin/ffprobe'
#cascPath = sys.argv[1]
#face_cascade = cv2.CascadeClassifier('/Users/oscardolloway/Documents/GitHub/LogoDetection/haarcascade_frontalface_default.xml')
#Video = '/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/jelly.mp4'

#video_capture = cv2.VideoCapture(0)

m3u8URL = ['http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8','http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8']
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
        

#img1 = mpimg.imread('/Users/oscardolloway/Documents/GitHub/LogoDetection/greyimages/'+str(i))
viddir = (os.path.dirname(os.path.abspath(sys.argv[0])))
print(viddir)
#files = os.listdir(viddir)
output_dir = os.path.abspath(os.path.curdir)
VIDEO_URL = m3u8URL

import time
def storingtest1():
    
    
    cap_dur = 5
    cap_num = 1
    print(cap_num)
    for urls in range(len(m3u8URL)):
        print(m3u8URL[urls])
        
        cmd = [ffprobe] + '-show_format -pretty -loglevel quiet'.split()+[m3u8URL[urls]]
        ffout = sp.check_output(cmd).decode('utf-8')
        print(ffout)
        
        cap = cv2.VideoCapture(m3u8URL[urls])
    
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# gets the correct height&width of live vid
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
       
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')#video type
        out = cv2.VideoWriter((str(cap_num)+'.mp4'),fourcc,24,(int(width),int(height)))
        #current_frame = 0
    
        cap_num = cap_num +1#stores us to store new videos
    
        start_time = time.time()
        print(start_time)
        while (int(time.time() - start_time)<cap_dur):
        
            ret, frame = cap.read()
        
            if ret == True:
            
                #frame = cv2.flip(frame,current_frame)
            #print(frame)
            #fshape = frame.shape
            #height= fshape[0]
            #width = fshape[1]
            
                frame = cv2.flip(frame,180)# allows us to store the video, without only 1 frames stores
                out.write(cv2.flip(frame, 180))
                
            #print(out.get(cv2.CAP_PROP_POS_MSEC))
            else:
                
                break
            
            
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        
        #print(out.get(cv2.CAP_PROP_POS_MSEC))
       
    #print('a',a_count)
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    cap_num = cap_num +1
        
        
# =============================================================================
#storingtest1()
# =============================================================================
from pathlib import Path
def getvidmeta ():
    data =  [ ffprobe, "-show_format", 
             "-f", "ffmetadata", 'in.txt']
    pipe = sp.Popen(data, stdout = sp.PIPE,bufsize=10**8)
    framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT ) 
    frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
   
    
#getvidmeta()
def probe_file(filename):
    #ffprobe -show_format -show_streams -loglevel quiet -print_format json YOUR_FILE
    pipe = sp.Popen([ FFMPEG_BIN, "-i", filename,
            # no text output
               # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-r",'1',
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)
  
    out =  pipe.communicate()
    
    import pickle
    dataset = ['hello','test']
    outputFile = 'test.data'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
#    print(ffout)
    #duration = sp.check_output([ffprobe, '-i', 'video.mp4', '-show_entries', 'format=duration', '-v', 'quiet'])
    
    #print(duration)
    
    #cmnd = ['ffprobe', '-v quiet -print_format json  -show_format, -show_streams',filename]
    #cmnd = [ffprobe , '-i', filename, '-show_entries' ,  'frame=pkt_pts_time,pkt_duration_time,interlaced_frame']
    #p = sp.Popen(cmnd, stdout=sp.PIPE, stderr=sp.PIPE)
    #p1 = sp.Popen(json, stdout=sp.PIPE, stderr=sp.PIPE)
    #print (filename)
    #out, err =  p.communicate()
    #out1, err =  p1.communicate()
    #print ("==========output==========")
    #print (out)
    #print(out1)
    #if err:
    #    print ("========= error ========")
    #    print (err)

#probe_file('1.mp4')


def beginnerscraper():
    url = "http://xmtvplayer.com/snippet/sample-m3u-file"
    #content = global
    site = urlopen(url).read()
    #print(site)
    try:
        page = urlopen(url)
    except:
        print('site not valid')
        sys.exit()
    response = get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(site,features="lxml",)
    content = soup.find_all("p", {"class": "box"},"")
    b = soup.find_all("p")
    content =  soup.find_all("p", {"class": "box"},"")
    All = soup.text
    links = re.findall("(?P<element>[\w\.\/\-\\:]+m3u8?)",All)
    links = set(links)
    #x = re.search("(?P<element>(https?)[\w\.\/\-\\:]+)",All)
    print(', '.join(links))
    #print(len(links))
#beginnerscraper()
url = 'http://www.example.com'
def webcheck (url):
    
    
    try:
        request = requests.get(url)
        print(request)
        if request.status_code == 200 :
            return True
    except ConnectionError as e:    # This is the correct syntax
        print('hello')
        request = 'no response'
        
        
#webcheck (url)
#if webcheck (url) == True:
#    print('hello')