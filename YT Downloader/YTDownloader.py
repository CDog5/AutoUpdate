import pytube
def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('./Output')
def download_playlist(url):
    playlist = pytube.Playlist(url)
    for vid in playlist.video_urls:
        download_video(vid)

