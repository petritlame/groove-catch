from pytube import Playlist
from bs4 import BeautifulSoup
import requests


def fetch_playlist_videos(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist_id = playlist_url.split("list=")[-1]
        video_data = [
            {
                "video_id": video_url.split("v=")[-1].split("&")[0],  # Extract video ID from the URL
                "playlist_id": playlist_id,
                "url": video_url
            }
            for video_url in playlist.video_urls
        ]
        return video_data
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []


def get_playlist_title(playlist_url):
    try:
        response = requests.get(playlist_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("meta", property="og:title")
        if title_tag:
            return title_tag["content"]
        return None
    except Exception as e:
        print(f"Error fetching playlist title: {e}")
        return None


def ask_yes_or_no(prompt):
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please respond with 'yes' or 'no'.")