import os
import time
from dotenv import load_dotenv
from app.services.youtube_service import fetch_playlist_videos, ask_yes_or_no, get_playlist_title
from app.helpers.db_helper import create_database, save_videos_to_db, get_videos_from_db, update_video
from app.services.download_service import download_audio, to_snake_case
load_dotenv()


def main():
    playlist_id = input("Enter the YouTube playlist ID: ")

    if not playlist_id:
        playlist_id = os.getenv("DEFAULT_PLAYLIST_ID")

    if not playlist_id:
        print("Error: No playlist ID provided and none found in .env.")
        return

    print("Fetching videos from the playlist...")
    playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'
    playlist_title = get_playlist_title(playlist_url)

    download_dir = f'playlists/{to_snake_case(playlist_title)}'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    videos = fetch_playlist_videos(playlist_url)
    if videos:
        print(f"Fetched {len(videos)} videos. Saving to database...")
        create_database()
        save_videos_to_db(videos, playlist_title)
        proceed_download = ask_yes_or_no("Do you want to download these songs inside playlist?")

        if proceed_download:
            videos_ids = get_videos_from_db()

            if not videos_ids:
                print("No videos found.")
                return

            for video in videos_ids:
                try:
                    download_audio(video['url'], download_dir)
                    update_video(video['video_id'])
                except Exception as e:
                    print(f"Error downloading {video['url']}: {str(e)}")
                time.sleep(1)
            print("Videos have been successfully saved to the database and downloaded")
        else:
            print("Videos have been successfully saved to the database.")
    else:
        print("Error: Could not fetch videos. Please check the playlist URL.")


if __name__ == "__main__":
    main()
