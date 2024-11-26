# 🎵 YouTube Playlist Downloader for Music Lover 🎵

A Python tool designed for DJs and music enthusiasts that fetches a YouTube playlist by its ID, downloads all songs as MP3 files, and stores metadata in a MariaDB database.

---

## Features
- Download all videos from a YouTube playlist as MP3.
- Manage playlist metadata using a MariaDB database.
- Optimized for Ubuntu users.
- Supports essential libraries for video and audio processing.

---

## Requirements
Before using this tool, ensure your system has the following:
- **Python**: Version 3.7 or higher
- **MariaDB**: Installed and configured
- **Ubuntu Packages**:
  - `libmariadb3`
  - `libmariadb-dev`
  - `ffmpeg`

To install the required Ubuntu packages, run:
```bash
sudo apt-get update
sudo apt-get install libmariadb3 libmariadb-dev ffmpeg
```
**Python dependencies**:
  - `pytube`
  - `python-dotenv`
  - `mariadb`
  - `beautifulsoup4`
  - `requests`
  - `yt_dlp`