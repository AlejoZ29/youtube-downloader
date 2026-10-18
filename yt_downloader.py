import os
from yt_dlp import YoutubeDL


def download_youtube(url, output_path, download_type="video"):
  if not os.path.exists(output_path):
    os.makedirs(output_path)

  ydl_opts = {
      "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
  }

  ffmpeg_path = os.path.expanduser(
      r"~\AppData\Local\Microsoft\WinGet\Packages"
  )
  if os.path.exists(ffmpeg_path):
    for root, dirs, files in os.walk(ffmpeg_path):
      if "ffmpeg.exe" in files:
        ydl_opts["ffmpeg_location"] = root
        break

  if download_type == "audio":
    ydl_opts.update({
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    })
  else:
    ydl_opts.update({
        "format": "bestvideo+bestaudio/best",
    })

  with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

  print(
      f"Download completed successfully to:"
      f" {os.path.abspath(output_path)}"
  )


if __name__ == "__main__":
  default_path = r"C:\Users\Alejandro\Documents\Videos Random"

  print("=== YouTube Downloader ===")
  url = input("Enter the YouTube URL: ").strip()

  download_type_input = (
      input("Do you want [v]ideo or [a]udio? (default: video): ")
      .strip()
      .lower()
  )
  download_type = (
      "audio" if download_type_input in ["a", "audio"] else "video"
  )

  path_input = input(
      f"Enter destination path (Press Enter to use default):\n[{default_path}]: "
  ).strip()
  destination_path = path_input if path_input else default_path

  print("\nStarting download...")
  download_youtube(url, destination_path, download_type=download_type)