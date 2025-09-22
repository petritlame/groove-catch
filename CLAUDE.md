# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
A Python application that downloads YouTube playlist videos as MP3 audio files and manages metadata in a MariaDB database. Designed for DJs and music enthusiasts.

## Development Commands

### Setup
```bash
# Install system dependencies (Ubuntu)
sudo apt-get update
sudo apt-get install libmariadb3 libmariadb-dev ffmpeg

# Install Python dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
python main.py
```

## Architecture

### Core Components
- **main.py**: Entry point that orchestrates playlist fetching, database operations, and audio downloads
- **app/services/youtube_service.py**: Handles YouTube playlist data fetching using pytube and web scraping
- **app/services/download_service.py**: Audio download functionality using yt-dlp with MP3 conversion
- **app/helpers/db_helper.py**: Database operations for video metadata storage and tracking
- **app/database/connection.py**: MariaDB connection management with environment variable configuration

### Database Schema
The application uses a `videos` table with:
- `video_id` (unique): YouTube video identifier
- `playlist_id`: YouTube playlist identifier
- `playlist_name`: Human-readable playlist name
- `url`: Full YouTube video URL
- `is_downloaded`: Boolean flag tracking download status

### Key Dependencies
- **pytube**: YouTube playlist and video data extraction
- **yt-dlp**: Audio downloading and format conversion
- **mariadb**: Database connectivity
- **beautifulsoup4**: HTML parsing for playlist metadata
- **python-dotenv**: Environment variable management

### Environment Configuration
The application requires a `.env` file with MariaDB connection details:
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
- `DEFAULT_PLAYLIST_ID` (optional)

### Download Flow
1. Fetch playlist videos using pytube
2. Store video metadata in MariaDB
3. Download audio files to `playlists/{playlist_name}` directory using yt-dlp
4. Mark videos as downloaded in database to prevent re-downloading