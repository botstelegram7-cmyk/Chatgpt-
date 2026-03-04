import os

def url_type(url: str):
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    if url.endswith(".mp4"):
        return "video"
    return "generic"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)