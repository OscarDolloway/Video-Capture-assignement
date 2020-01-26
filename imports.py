#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:04:19 2020

@author: oscardolloway
"""

    #from __future__ import print_function
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


def Capture(url):
    num_sites = len(url)
    
    cap = cv2.VideoCapture(url)
    
    cap_num = 1
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter((str(cap_num)+'live.mp4'),fourcc,24,(int(width),int(height)))
    current_frame = 0
    
    a_count = 0
    
    while (cap.isOpened()):
        
        ret, frame = cap.read()
        a_count = a_count + 1
        
        if ret == True:
    
            a = cv2.imshow("video", frame)
            out.write(cv2.flip(frame, 180))
        else:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        current_frame +=1
    cap.release()
    out.release()
    cv2.destroyAllWindows()