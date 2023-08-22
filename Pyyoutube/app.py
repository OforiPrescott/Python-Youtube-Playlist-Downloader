import os
from pytube import YouTube, Playlist

FULL_PATH = os.path.abspath(".")
PLAYLIST_URL = input("Enter the playlist link: ")

try:
    playlist = Playlist(PLAYLIST_URL)
except Exception as e:
    print("An error occurred while fetching the playlist:", e)
    exit(1)

path = os.path.join(FULL_PATH, playlist.title)

if not os.path.exists(path):
    os.makedirs(path)

for url in playlist.video_urls:
    try:
        video = YouTube(url)
        print(f"Downloading {video.title}")

        video_path = os.path.join(path, f"{video.title}.mp4")

        if os.path.exists(video_path):
            print("Video already exists. Skipping...")
            continue

        stream = video.streams.get_highest_resolution()
        if stream:
            stream.download(output_path=path)
            print("Download completed.")
        else:
            print("No suitable streams found for this video.")

    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
