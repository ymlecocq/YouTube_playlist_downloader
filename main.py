import re   # libray that fixes the empty playlist.videos list

from pytube import Playlist
from pytube import YouTube
from pytube.innertube import _default_clients

# pour éviter l'erreur liée à la restriction d'age
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream

DOWNLOAD_DIR = 'H:\\& Download\\Bass_BT'


# on crée l'objet playlist qui va lire l'URL où sont stockées les playlists

# playlist = Playlist('https://www.youtube.com/playlist?list=PLntaM2Y0E0mXqStadUedgq3WyOzE_S3Mf')       # Best BT
playlist = Playlist('https://www.youtube.com/playlist?list=PLntaM2Y0E0mXwKGpJclsW7l4rWNc5JWKL')         # Bass BT

print(type(playlist))

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print("Nombre de fichiers : ",len(playlist.video_urls))

# for url in playlist.video_urls:
#     print(url)

# physically downloading the audio track
i = 0
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    print(i, " : ",audioStream)
    i += 1
    audioStream.download(output_path=DOWNLOAD_DIR)