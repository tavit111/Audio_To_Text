from transcribe import transcribe_audio_file
from files import convert_mp3_to_wav
from files import delete_file
from files import write_text_to_file
from files import is_wav_file
from files import directory_to_text_file
from files import list_files_in_directory
import os


def transcript_audio(audio_path, language_name):
    # transcribe audio file (mp3, wav) and return the text
    tempFile = False
    if is_wav_file(audio_path):
        wav_path = audio_path
    else:
        wav_path = convert_mp3_to_wav(audio_path)
        tempFile = True

    transcription = transcribe_audio_file(wav_path, language_name)

    if tempFile:
        delete_file(wav_path)

    return transcription


def audio_file_to_text(audio_path, language_name):
    # transcribe one audio (mp3, wav) file to one text file with the same name
    transcription = transcript_audio(audio_path, language_name)
    text_path = os.path.splitext(audio_path)[0]
    write_text_to_file(text_path, transcription)


def audio_files_to_texts(directory_path, language_name):
    # transcribe many audio (mp3, wav) files to many text files with the same names
    if not os.path.isdir(directory_path):
        raise Exception("not a directory path")

    audio_paths = list_files_in_directory(directory_path)
    for audio_path in audio_paths:
        audio_file_to_text(audio_path, language_name)


def audio_files_to_text(directory_path, language_name):
    # transcribe many audio (mp3, wav) files to one text file each audio file is a new line. Text file with the same directory name
    if not os.path.isdir(directory_path):
        raise Exception("not a directory path")

    audio_paths = list_files_in_directory(directory_path)
    transcription_list = ''
    for audio_path in audio_paths:
        transcription = transcript_audio(audio_path, language_name)
        transcription_list += f"{transcription}\n"

    text_path = directory_to_text_file(directory_path)
    write_text_to_file(text_path, transcription_list)


audio_files_to_texts(
    '/home/tavit/Code/Audio_To_Text/media/test 2 - result/', 'spanish')
