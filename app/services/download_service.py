from yt_dlp import YoutubeDL
import os
import re


def download_audio(url, download_dir):
    """
    Download audio from a YouTube URL and save it to the specified directory.

    :param url: The YouTube video URL.
    :param download_dir: The directory where the audio file will be saved.
    """
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_dir}/%(title)s',  # Use the dynamic directory
        'verbose': True,  # Enables verbose output for debugging
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading audio: {e}")


def clean_title(title, patterns):
    for pattern in patterns:
        title = re.sub(pattern, '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def rename_downloaded_file(d):
    if d['status'] == 'finished':
        old_filename = d['filename']
        title = d['info_dict']['title']
        cleaned_title = clean_title(title)
        new_filename = os.path.join('songs', f"{cleaned_title}")
        os.rename(old_filename, new_filename)
        print(f"Downloaded and saved: {new_filename}")


def to_snake_case(text):
    text = re.sub(r'[\s-]+', '_', text)
    text = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', text)
    text = text.lower()
    text = text.strip('_')
    return text
