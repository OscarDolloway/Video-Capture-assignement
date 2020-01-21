# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 01:02:37 2018

@author: oscar
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
#import Differentimages as ImgFilt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
import subprocess as sp
import time
FFMPEG_BIN = "ffmpeg"
#VIDEO_URL = "http://www.bokowsky.net/de/knowledge-base/video/hls_bunny/7ea96983ed10dc5546f8275871a38df7_127912_60594786.m3u8"


def videoread(URL):
#VIDEO_URL = "http://www.bokowsky.net/de/knowledge-base/video/hls_bunny/7ea96983ed10dc5546f8275871a38df7_127912_60594786.m3u8"
    cam = cv2.VideoCapture(URL)
    cv2.namedWindow("GoPro",cv2.WINDOW_AUTOSIZE)
    while True:
        f, im = cam.read()
        cv2.imshow("GoPro",im)
        if cv2.waitKey(5) == 27:
            break
        cam.release()
        cv2.destroyAllWindows()
videoread('/Users/oscardolloway/Documents/SampleVideo_1280x720_1mb.mp4')
video = '/Users/oscardolloway/Documents/SampleVideo_1280x720_1mb.mp4'


def m3u8read (URL):

#URL = "http://www.bokowsky.net/de/knowledge-base/video/hls_bunny/7ea96983ed10dc5546f8275871a38df7_127912_60594786.m3u8"
    #greyvid = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

    cv2.namedWindow("GoPro",cv2.WINDOW_AUTOSIZE)

    pipe = sp.Popen([ FFMPEG_BIN, "-i", URL,
                     "-loglevel", "quiet", # no text output
                     "-an",   # disable audio
                     "-ss","1", 
                     "-f", "image2pipe",
                     "-pix_fmt", "bgr24",
                     "-vcodec", "rawvideo", "-"],
               stdin = sp.PIPE, stdout = sp.PIPE)
    while True:
        #raw_image = pipe.stdout.read(432*240*3) # read 432*240*3 bytes (= 1 frame)
        image =  np.fromstring(URL, dtype='uint8')
        greyvid = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("GoPro",greyvid)
        time.sleep( 1.0)
        if cv2.waitKey(5) == 27:
            break
        cv2.destroyAllWindows()
        
m3u8read('/Users/oscardolloway/Documents/SampleVideo_1280x720_1mb.mp4')







