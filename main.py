from transcribe import transcribe_audio_file
from files import convert_mp3_to_wav
from files import delete_file


mp3_file_path = './media/1.mp3'
wav_file_path = convert_mp3_to_wav(mp3_file_path)
transcription = transcribe_audio_file(wav_file_path, 'spanish')
print(transcription)
delete_file(wav_file_path)
