# YouTube to Mp3

A simple application that downloads either a single song or playlist form YouTube to MP3 audio. Uses the [youtube-dl](https://github.com/ytdl-org/youtube-dl) library with **pip** install. 

_This application was created using Python 3.7 with a conda virtual environment_

### Make sure you install **youtube-dl**

```
pip install --upgrade youtube-dl
```

## How to use

1. Set the variables: 
    > youtube_url
    
    `String` URL value. It can be either a single video URL or playlist URL.
    
    > file_path

    `String` directory and file path. The directory must exist. In the file_path sample there is a `test/` directory. This folder must be created, changed, or removed. 
    
2. Set the `ydl_opts` ( _youtube download options_ )

    > `'noplaylist'`: True

    Set this to `False` when the `youtube_url` is using a playlist

    > `'playliststart'`: 1

    Defines which video to **START** from in a playlist. _Commented out by default._

    > `'playlistend'`: 10

    Defines which video to **END** at in a playlist. _Commented out by default._

3. In the `terminal` or `cmd` run

```
python YouTubeToMp3.py
```


## Additional - Download Options

You can find additonal options/settings for the `ydl_opts` dictionary @ [https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/options.py](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/options.py) 

Search for the option you want to include and use the `dest` keyword as the `key` in the `ydl_opts` dictionary.

Example:

```python
'--playlist-end',
dest='playlistend', metavar='NUMBER', default=None, type=int,
help='Playlist video to end at (default is last)'
```
