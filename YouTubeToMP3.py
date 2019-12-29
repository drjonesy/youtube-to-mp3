from __future__ import unicode_literals
import youtube_dl

# this can either be a single video link or a playlist.
# if it is a playlist, make sure to set noplaylist to True if you want to group the songs
# youtube_url='https://www.youtube.com/watch?v=uT3SBzmDxGk' # single video
youtube_url='https://www.youtube.com/watch?v=uT3SBzmDxGk&list=RDEM3VGq8Ysq0P67pRncwzau9A&start_radio=1' # playlist
# define folder path and meta options for file, the folder path must exist
# I had to create the 'test' folder
file_path = 'test/%(title)s.mp3' 

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

ydl_opts = {
    'format': 'mp3/worstvideo', # by selecting worstvideo the file size is reduced
    'outtmpl': file_path,
    'progess_hooks': [my_hook],
    'ignoreerrors': True,
    'noplaylist': False, # set to True for single video
    'playliststart': 1,  # defines which video to start from in a playlist
    'playlistend': 10,   # defines which video to end at in a playlist
}

with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
    ydl.download(url_list=[youtube_url])


# with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
    # meta = ydl.extract_info(url=youtube_url, download=False)

# for k,v in list(meta.items())[:12]:
#     print(f"{k}: {v}")
