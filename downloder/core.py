import yt_dlp
import os
from config import DL_DIR

def download(url):
    os.makedirs(DL_DIR, exist_ok=True)
    ydl_opts = {
        "outtmpl": f"{DL_DIR}/%(title)s.%(ext)s",
        "quiet": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)