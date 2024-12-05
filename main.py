from pychorus import find_and_output_chorus,find_chorus
from mutagen.mp3 import MP3

def get_song_duration(file_path):
    audio = MP3(file_path)
    duration = audio.info.length
    return duration

file_path = 'path/to/your/song.mp3'
duration = get_song_duration(file_path)
print(f"{duration}")