# YouTube Downloader

A simple and interactive Python script to download YouTube videos or extract audio (MP3) using `yt-dlp` and `ffmpeg`, with support for custom or default destination paths.

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python** (version 3.8 or higher recommended)
2. **FFmpeg** (required for audio extraction/MP3 conversion). If you are on Windows, you can easily install it via terminal:
   ```bash
   winget install Gyan.FFmpeg
   ```

## Installation

1. Clone or download this repository to your local machine.
2. Open your terminal in the project directory and install the required library:
   ```bash
   pip install yt-dlp
   ```

## Usage

Run the script directly from your terminal:

```bash
python yt_downloader.py
```

The script will interactively prompt you for:
1. **The YouTube URL**: Paste the link of the video you want to download.
2. **Type**: Choose between `v` (video) or `a` (audio/MP3). Pressing Enter defaults to video.
3. **Destination Path**: Enter a custom folder path, or simply press **Enter** to use the default path (`C:\Users\Alejandro\Documents\Videos Random`).