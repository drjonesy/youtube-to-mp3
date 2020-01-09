from __future__ import unicode_literals
import youtube_dl

import moviepy.editor as mp
import os
import glob

# ================= FUNCTIONS ==============
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

def PAUSE(s):
    print(s)
    input('....waiting...')


# ------------------------------------------------------------------------------
# ============= VIDEO URL ============================|| Video or Playlist
# ------------------------------------------------------------------------------
youtube_url='https://www.youtube.com/watch?v=uT3SBzmDxGk'
# ==============================================================================


basedir = os.path.abspath(os.path.dirname(__file__))
saveDir = os.path.join(basedir,'test')
# ------------------------------------------------------------------------------
# ============= Where to Save Files =======================|| Video or Playlist
# ------------------------------------------------------------------------------
mp4FileNameAndPath = os.path.join(saveDir, '%(title)s.mp4') 
# ==============================================================================

# ------------------------------------------------------------------------------
# ============= Youtube-dl  =======================|| Settings
# ------------------------------------------------------------------------------

ydl_opts = {
    # 'format': 'worstvideo', # by selecting worstvideo the file size is reduced
    'format': 'mp4/worstvideo',
    'outtmpl': mp4FileNameAndPath,
    'progess_hooks': [my_hook],
    'ignoreerrors': True,
    'noplaylist': False, # set to True for single video
    # 'playliststart': 1,  # defines which video to start from in a playlist
    # 'playlistend': 10,   # defines which video to end at in a playlist
}
# ==============================================================================

if __name__ == "__main__":
    
    # ------------------------------------------------------------------------------
    # ============= Download Mp4  =======================|| Video or Playlist
    # ------------------------------------------------------------------------------
    with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
        ydl.download(url_list=[youtube_url])
    # ==============================================================================


    # ------------------------------------------------------------------------------
    # ============= Retrieve Meta Data  =======================|| Video or Playlist
    # ------------------------------------------------------------------------------
    # with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
        # meta = ydl.extract_info(url=youtube_url, download=False)

    # for k,v in list(meta.items())[:12]:
    #     print(f"{k}: {v}")
    # ==============================================================================


    # ------------------------------------------------------------------------------
    # ============= Covert to Mp3  =======================|| Video or Playlist
    # ------------------------------------------------------------------------------
    fileList = glob.glob(os.path.join(saveDir, '*.mp4') )



    for filePath in fileList:
        # change audio file extension
        audioFilePath = f"{os.path.splitext(filePath)[0]}.mp3"
        audio = mp.AudioFileClip(filename=filePath)
        audio.write_audiofile(filename=audioFilePath)
        # remove Mp4 file
        os.remove(filePath)

