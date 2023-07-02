from pydub import AudioSegment
import os
import re


def convert_mp3_to_wav(mp3_file_path):
    # convert mp3 file to wav with the same name and path, returns path to the wav
    fileNamePath = os.path.splitext(mp3_file_path)[0]
    wav_file_path = fileNamePath + ".wav"
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")
    return wav_file_path


def delete_file(file_path):
    # delate file
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while deleting file '{file_path}': {str(e)}")


def write_text_to_file(file_path, text):
    try:
        with open(file_path, "w") as file:
            file.write(text)
        print(f"Text written to file '{file_path}' successfully.")
    except FileNotFoundError:
        print(f"Directory for file '{file_path}' not found.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except PermissionError:
        print(f"Permission denied to write to file '{file_path}'.")
    except Exception as e:
        print(
            f"An error occurred while writing text to file '{file_path}': {str(e)}")


def is_wav_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    return extension == ".wav"


def is_mp3_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    return extension == ".mp3"


def directory_to_text_file(directory_path):
    last_directory_name = os.path.basename(os.path.normpath(directory_path))
    text_file_path = os.path.join(directory_path, last_directory_name)
    return text_file_path


def natural_sort(strings):
    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split('([0-9]+)', key)]

    sorted_strings = sorted(strings, key=alphanum_key)
    return sorted_strings


def list_files_in_directory(directory_path):
    file_paths = []
    files = os.listdir(directory_path)
    filtered_files = [file for file in files if is_mp3_file(
        file) or is_wav_file(file)]
    sorted_files = natural_sort(filtered_files)
    for file in sorted_files:
        file_path = os.path.join(directory_path, file)
        file_paths.append(file_path)

    filterd_paths = [path for path in file_paths if not os.path.isdir(path)]
    return filterd_paths
