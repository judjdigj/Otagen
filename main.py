from pychorus import find_and_output_chorus,find_chorus
from mutagen.mp3 import MP3

def get_song_duration(file_path):
    audio = MP3(file_path)
    duration = audio.info.length
    return duration

file_path = 'maou_08_burning_heart.mp3'
duration = get_song_duration(file_path)
## print(f"{duration}")

chorus_start_sec = find_and_output_chorus("maou_08_burning_heart.mp3", "temp.mp3")
print(f"{chorus_start_sec}")