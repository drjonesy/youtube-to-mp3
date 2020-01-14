from __future__ import unicode_literals
import youtube_dl

import moviepy.editor as mp
import os
import glob

import time

# ================ INITIALIZE BASE DIRECTORY ==============
base_dir = os.path.abspath(os.path.dirname(__file__))
# ================= FUNCTIONS =============================
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

def PAUSE(s):
    print(s)
    input('....waiting...')
    
def YouTubeToMp3(url: str, path: str):

    folders = [val for val in path.replace('\\', '/').split('/') if val != '']
    save_dir = os.path.join(base_dir, 'audio', *folders)
    mp4FileNameAndPath = os.path.join(save_dir, '%(title)s.mp4') 

    ydl_opts = {
        # 'format': 'worstvideo', # by selecting worstvideo the file size is reduced
        'format': 'mp4/worstvideo',
        'outtmpl': mp4FileNameAndPath,
        'progess_hooks': [my_hook],
        'ignoreerrors': True,
        'noplaylist': False,
    }

    with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
        # Start a Timer for Downloading
        ydl.download(url_list=[url])

                
    # End Download Timer

    # ------------------------------------------------------------------------------
    # ============= Covert to Mp3  =======================|| Video or Playlist
    # ------------------------------------------------------------------------------
    
    # Start New Timer for Conversion 
    fileList = glob.glob(os.path.join(save_dir, '*.mp4') )

    for filePath in fileList:
        # change audio file extension
        audioFilePath = f"{os.path.splitext(filePath)[0]}.mp3"
        audio = mp.AudioFileClip(filename=filePath)
        audio.write_audiofile(filename=audioFilePath)
        # remove Mp4 file
        os.remove(filePath)
    
    # Stop Conversion Timer

