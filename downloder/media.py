import subprocess

def generate_thumb(video, thumb):
    subprocess.run([
        "ffmpeg","-y","-ss","3","-i",video,"-frames:v","1",thumb
    ])