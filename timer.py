#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:09:24 2020

@author: oscardolloway
"""
FFMPEG_BIN ='/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/ffmpeglib/bin/ffmpeg'
import time

#run = input("Start? > ")
mins = 0
sec = 0
# Only run if the user types in "start"
#if run == "start":
    # Loop until we reach 20 minutes running
   # while sec != 10:
   #     print(">>>>>>>>>>>>>>>>>>>>> {}".format(sec))
   #     # Sleep for a minute
   #     time.sleep(1)
   #     sec += 1
   #     if sec == 60:
    #        mins+=1
        # Increment the minute total
        #mins += 1
        
        
from pathlib import Path
import subprocess as sp

def video_length_seconds(filename):
    result = sp.run(
        [FFMPEG_BIN,
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            filename,
        ],
        capture_output=True,
        text=True,
    )
# a single video
print(sum(video_length_seconds(f) for f in Path('/Users/oscardolloway/Documents/GitHub/Video-Capture-assignement/').glob("*.mp4")))
