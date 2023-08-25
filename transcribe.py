import speech_recognition as sr


language_codes = {
    'english': 'en-US',
    'british': 'en-GB',
    'spanish': 'es-ES',
    'french': 'fr-FR',
    'italian': 'it-IT',
    'portuguese': 'pt-PT',
    'german': 'de-DE',
    'japanese': 'ja-JP',
    'korean': 'ko-KR',
    'indonesian': 'id-ID',
    'russian': 'ru-RU',
    'chinese': 'zh',
    'swedish': 'sv-SE'
}


def transcribe(wav_file_path, language_name):
    # take 1 wav file  and language in writen format (lowcap: spanish, japanese)
    # return transcyption
    recognizer = sr.Recognizer()
    language_code = language_codes[language_name]

    with sr.AudioFile(wav_file_path) as audio_file:
        audio = recognizer.record(audio_file)

    transcript = ""
    try:
        transcript = recognizer.recognize_google(
            audio, language=language_code, show_all=False)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

    return transcript


def transcribeSegment(segment, language_name):
    # take 1 wav file  and language in writen format (lowcap: spanish, japanese)
    # return transcyption
    raw_data = segment.raw_data
    recognizer = sr.Recognizer()
    language_code = language_codes[language_name]

    transcript = ""
    try:
        transcript = recognizer.recognize_google(
            raw_data, language=language_code, show_all=False)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

    return transcript
