from pydub import AudioSegment
import os


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
