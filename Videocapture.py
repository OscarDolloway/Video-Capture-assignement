#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:13:35 2020

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
from requests.exceptions import HTTPError
from imports import Capture
import imports

current_dir = (os.path.dirname(os.path.abspath(sys.argv[0])))#current directory
files = os.listdir(current_dir)#files within the current directory

FFMPEG_BIN = current_dir + '/ffmpeglib/bin/ffmpeg'
ffprobe = current_dir + '/ffmpeglib/bin/ffprobe'


# =============================================================================
# Step one -- Check what URL has been entered & check if site is valid
# =============================================================================

url = ['http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8','http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8']

def urlcheck():
    for urls in ['ef',url]:
        try:
            response = requests.get(urls)
    
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            return True
            print('Success!')
            
            
if urlcheck() == True:
    print('working')
    if 'm3u8' in url:
        print("URL contains m3u8, Running capture")
        Capture('http://95.170.215.120/hls/m3u8/BT-Sport-1HD.m3u8')

