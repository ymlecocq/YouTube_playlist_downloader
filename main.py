import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'H:\\& Download\\Best_BT'

playlist = Playlist('https://www.youtube.com/playlist?list=PLntaM2Y0E0mXqStadUedgq3WyOzE_S3Mf')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)