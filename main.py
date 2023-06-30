from transcribe import transcribe_audio_file
from files import convert_mp3_to_wav
from files import delete_file
from files import write_text_to_file
import os


files = os.listdir('./media')
result = {}
for file in files:
    language_name = os.path.splitext(file)[0]
    path = "./media/" + file
    mp3_file_path = path
    wav_file_path = convert_mp3_to_wav(mp3_file_path)
    transcription = transcribe_audio_file(wav_file_path, language_name)
    write_text_to_file(language_name, transcription)
    delete_file(wav_file_path)
