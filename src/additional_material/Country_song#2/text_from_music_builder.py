# import speech_recognition as sr
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from pytube import YouTube
# from pydub import AudioSegment

# # Funktion för ljudtranskription
# def transcribe_audio(audio_file):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source)  # Läs in ljudfilen
#     text = recognizer.recognize_google(audio_data, language="en-US")  # Transkribera ljudet till text
#     return text

# # Funktion för texttolkning
# def analyze_text(text):
#     # Tokenisera texten
#     tokens = word_tokenize(text)
    
#     # Sentimentanalys med NLTK's Vader
#     sid = SentimentIntensityAnalyzer()
#     sentiment_scores = sid.polarity_scores(text)
#     sentiment = "neutral"
#     if sentiment_scores["compound"] > 0:
#         sentiment = "positiv"
#     elif sentiment_scores["compound"] < 0:
#         sentiment = "negativ"
    
#     # Visa resultat
#     print("Text:", text)
#     print("Tokeniserade ord:", tokens)
#     print("Sentiment:", sentiment)
#     print("Sentiment-scores:", sentiment_scores)

# # Funktion för att ladda ner ljud från en YouTube-video och spara det som WAV
# def download_youtube_audio(video_url):
#     yt = YouTube(video_url)
#     audio_stream = yt.streams.filter(only_audio=True).first()
#     audio_file = audio_stream.download()  # Sparar ljudfilen i samma mapp som detta skript
#     return audio_file

# # Exempel på användning
# video_url = "https://www.youtube.com/watch?v=8bxs6O3ipLw"
# audio_file = download_youtube_audio(video_url)

# # Extrahera ljudet från videon och spara det som WAV
# audio = AudioSegment.from_file(audio_file)
# audio_file_wav = "audio.wav"
# audio.export(audio_file_wav, format="wav")

# # Transkribera ljudet och analysera texten
# transcribed_text = transcribe_audio(audio_file_wav)
# analyze_text(transcribed_text)

#===============================================================

# import os
# import speech_recognition as sr
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from pydub import AudioSegment

# # Funktion för ljudtranskription
# def transcribe_audio(audio_file, timeout=10):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source, duration=timeout)  # Läs in ljudfilen med angiven timeout
#     text = recognizer.recognize_google(audio_data, language="en-US", show_all=True)  # Transkribera ljudet till text
#     return text

# # Funktion för texttolkning
# def analyze_text(text):
#     # Tokenisera texten
#     tokens = word_tokenize(text)
    
#     # Sentimentanalys med NLTK's Vader
#     sid = SentimentIntensityAnalyzer()
#     sentiment_scores = sid.polarity_scores(text)
#     sentiment = "neutral"
#     if sentiment_scores["compound"] > 0:
#         sentiment = "positiv"
#     elif sentiment_scores["compound"] < 0:
#         sentiment = "negativ"
    
#     # Visa resultat
#     print("Text:", text)
#     print("Tokeniserade ord:", tokens)
#     print("Sentiment:", sentiment)
#     print("Sentiment-scores:", sentiment_scores)

# # Ange filnamnet på MP3-filen (om den finns i samma mapp som din Python-kod)
# mp3_file_name = "16 5 Leaf Clover.mp3"  # Obs! Byt ut filnamnet mot ditt eget

# # Skapa en absolut sökväg till MP3-filen
# script_directory = os.path.dirname(os.path.abspath(__file__))
# mp3_file_path = os.path.join(script_directory, mp3_file_name)

# # Konvertera MP3-filen till WAV-format med pydub
# audio = AudioSegment.from_mp3(mp3_file_path)
# wav_file_path = os.path.join(script_directory, "16 5 Leaf Clover.wav")
# audio.export(wav_file_path, format="wav")

# # Transkribera WAV-filen och utför sentimentanalys
# transcribed_text = transcribe_audio(wav_file_path, timeout=10)  # Set timeout to 10 seconds
# analyze_text(transcribed_text)




# import os
# import speech_recognition as sr
# from nltk.tokenize import word_tokenize
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from pydub import AudioSegment

# # Funktion för ljudtranskription
# def transcribe_audio(audio_file):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source)  # Läs in ljudfilen
#     text = recognizer.recognize_google(audio_data, language="en-US")  # Transkribera ljudet till text
#     return text

# # Funktion för texttolkning
# def analyze_text(text):
#     # Tokenisera texten
#     tokens = word_tokenize(text)
    
#     # Sentimentanalys med NLTK's Vader
#     sid = SentimentIntensityAnalyzer()
#     sentiment_scores = sid.polarity_scores(text)
#     sentiment = "neutral"
#     if sentiment_scores["compound"] > 0:
#         sentiment = "positiv"
#     elif sentiment_scores["compound"] < 0:
#         sentiment = "negativ"
    
#     # Visa resultat
#     print("Text:", text)
#     print("Tokeniserade ord:", tokens)
#     print("Sentiment:", sentiment)
#     print("Sentiment-scores:", sentiment_scores)

# # Ange filnamnet på MP3-filen (om den finns i samma mapp som din Python-kod)
# mp3_file_name = "16 5 Leaf Clover.mp3"  # Obs! Byt ut filnamnet mot ditt eget

# # Skapa en absolut sökväg till MP3-filen
# script_directory = os.path.dirname(os.path.abspath(__file__))
# mp3_file_path = os.path.join(script_directory, mp3_file_name)

# # Konvertera MP3-filen till WAV-format med pydub
# audio = AudioSegment.from_mp3(mp3_file_path)
# wav_file_path = os.path.join(script_directory, "16 5 Leaf Clover.wav")
# audio.export(wav_file_path, format="wav")

# # Transkribera WAV-filen och utför sentimentanalys
# transcribed_text = transcribe_audio(wav_file_path)
# analyze_text(transcribed_text)

#====================================

# import speech_recognition as sr
# from pydub import AudioSegment

# # Läs in MP3-filen
# audio_file = "16 5 Leaf Clover.mp3"
# sound = AudioSegment.from_mp3(audio_file)

# # Konvertera MP3 till WAV (SpeechRecognition stöder inte direkt MP3)
# sound.export("16 5 Leaf Clover.wav", format="wav")

# # Skapa en Recognizer-instans
# recognizer = sr.Recognizer()

# # Öppna WAV-filen och läs in ljudet
# with sr.AudioFile("16 5 Leaf Clover.wav") as source:
#     audio_data = recognizer.record(source)

# # Använd Google Speech Recognition för att konvertera ljud till text
# try:
#     text = recognizer.recognize_google(audio_data, language="sv-SE")
#     print("Konverterad text:")
#     print(text)
# except sr.UnknownValueError:
#     print("Kunde inte konvertera ljudet till text.")
# except sr.RequestError as e:
#     print(f"Kunde inte hämta resultat från Google Speech Recognition: {e}")

# from google.auth import credentials
# from google.cloud import speech_v1p1beta1 as speech

# # Ange din API-nyckel här
# api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# # Skapa en autentiseringenhet med din API-nyckel
# credentials_obj = credentials.AnonymousCredentials(api_key)

# # Skapa en klient för Google Speech-to-Text API med autentiseringsenheten
# client = speech.SpeechClient(credentials=credentials_obj)

# # Ange sökvägen till ljudfilen du vill transkribera
# audio_file = "16 5 Leaf Clover.wav"

# # Läs in ljudfilen
# with open(audio_file, "rb") as audio_file:
#     content = audio_file.read()

# # Definiera ljudinmatningen för transkriberingen
# audio = speech.RecognitionAudio(content=content)

# # Ange språket för ljudfilen, till exempel "sv-SE" för svenska
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     language_code="sv-SE"
# )

# # Anropa Google Speech-to-Text API för att transkribera ljudet
# response = client.recognize(config=config, audio=audio)

# # Hämta transkriptionen från svaret
# transcription = ""
# for result in response.results:
#     transcription += result.alternatives[0].transcript

# # Skriv ut transkriptionen
# print("Transkription:")
# print(transcription)



# from google.auth.credentials import AnonymousCredentials, Credentials
# from google.auth import exceptions
# from google.cloud import speech_v1p1beta1 as speech

# # Ange din API-nyckel här
# api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# # Skapa en autentiseringsenhet med din API-nyckel
# try:
#     credentials_obj = Credentials.from_api_key(api_key)
# except exceptions.RefreshError:
#     credentials_obj = AnonymousCredentials()

# # Skapa en klient för Google Speech-to-Text API med autentiseringsenheten
# client = speech.SpeechClient(credentials=credentials_obj)

# # Resten av koden fortsätter som tidigare


# from google.auth import credentials
# from google.cloud import speech_v1p1beta1 as speech

# # Ange din API-nyckel här
# api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# # Skapa en autentiseringenhet med din API-nyckel
# credentials_obj = credentials.AnonymousCredentials()

# # Skapa en klient för Google Speech-to-Text API med autentiseringsenheten
# client = speech.SpeechClient(credentials=credentials_obj)

# # Ange sökvägen till ljudfilen du vill transkribera
# audio_file = "16 5 Leaf Clover.wav"

# # Läs in ljudfilen
# with open(audio_file, "rb") as audio_file:
#     content = audio_file.read()

# # Definiera ljudinmatningen för transkriberingen
# audio = speech.RecognitionAudio(content=content)

# # Ange språket för ljudfilen, till exempel "sv-SE" för svenska
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     language_code="sv-SE"
# )

# # Anropa Google Speech-to-Text API för att transkribera ljudet
# response = client.recognize(config=config, audio=audio)

# # Hämta transkriptionen från svaret
# transcription = ""
# for result in response.results:
#     transcription += result.alternatives[0].transcript

# # Skriv ut transkriptionen
# print("Transkription:")
# print(transcription)


# from google.auth import credentials
# from google.cloud import speech_v1p1beta1 as speech
# from pydub import AudioSegment
# from google.api_core.exceptions import InvalidArgument

# # Ange din API-nyckel här
# api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# # Skapa en autentiseringsenhet med din API-nyckel
# credentials_obj = credentials.AnonymousCredentials()

# # Skapa en klient för Google Speech-to-Text API med autentiseringsenheten
# client = speech.SpeechClient(credentials=credentials_obj)

# # Ange sökvägen till ljudfilen du vill transkribera
# audio_file = "16 5 Leaf Clover.wav"

# # Läs in ljudfilen
# sound = AudioSegment.from_wav(audio_file)

# # Dela upp ljudfilen i segment på 5 sekunder
# segment_length_ms = 5000
# segments = [sound[i:i+segment_length_ms] for i in range(0, len(sound), segment_length_ms)]

# # Loopa genom varje segment och transkribera det separat
# transcription = ""
# for i, segment in enumerate(segments):
#     segment.export(f"segment_{i}.wav", format="wav")
#     audio_content = segment.raw_data
#     audio = speech.RecognitionAudio(content=audio_content)
    
#     # Ange språket för ljudfilen, till exempel "sv-SE" för svenska
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         language_code="sv-SE"
#     )
    
#     # Anropa Google Speech-to-Text API för att transkribera ljudet
#     try:
#         response = client.recognize(config=config, audio=audio)
#     except InvalidArgument as e:
#         print(f"Kunde inte transkribera segment {i}: {e}")
#         continue
    
#     # Hämta transkriptionen från svaret och lägg till i den totala transkriptionen
#     for result in response.results:
#         transcription += result.alternatives[0].transcript + " "

# # Skriv ut den slutliga transkriptionen
# print("Slutlig transkription:")
# print(transcription)



# from google.auth import exceptions
# from google.cloud import speech_v1p1beta1 as speech
# from pydub import AudioSegment

# # Ange din API-nyckel här
# api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# # Skapa en klient för Google Speech-to-Text API med autentiseringsnyckeln
# try:
#     client = speech.SpeechClient(credentials=api_key)
# except exceptions.RefreshError:
#     print("Ogiltig API-nyckel. Kontrollera din API-nyckel och försök igen.")
#     exit()

# # Ange sökvägen till ljudfilen du vill transkribera
# audio_file = "16 5 Leaf Clover.wav"

# # Läs in ljudfilen
# sound = AudioSegment.from_wav(audio_file)

# # Dela upp ljudfilen i segment på 5 sekunder
# segment_length_ms = 40000
# segments = [sound[i:i+segment_length_ms] for i in range(0, len(sound), segment_length_ms)]

# # Loopa genom varje segment och transkribera det separat
# transcription = ""
# for i, segment in enumerate(segments):
#     segment.export(f"segment_{i}.wav", format="wav")
#     audio_content = segment.raw_data
#     audio = speech.RecognitionAudio(content=audio_content)
    
#     # Ange språket för ljudfilen, till exempel "sv-SE" för svenska
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         language_code="sv-SE"
#     )
    
#     # Anropa Google Speech-to-Text API för att transkribera ljudet
#     try:
#         response = client.recognize(config=config, audio=audio)
#     except Exception as e:
#         print(f"Kunde inte transkribera segment {i}: {e}")
#         continue
    
#     # Hämta transkriptionen från svaret och lägg till i den totala transkriptionen
#     for result in response.results:
#         transcription += result.alternatives[0].transcript + " "

# # Skriv ut den slutliga transkriptionen
# print("Slutlig transkription:")
# print(transcription)


from google.auth import exceptions
from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment

# Ange din API-nyckel här
api_key = "AIzaSyBp9R0LV-hp0bRVN1IbhF9lFBs7_fIqZgw"

# Skapa en klient för Google Speech-to-Text API med autentiseringsnyckeln
try:
    client = speech.SpeechClient(credentials=api_key)
except exceptions.RefreshError:
    print("Ogiltig API-nyckel. Kontrollera din API-nyckel och försök igen.")
    exit()

# Ange sökvägen till ljudfilen du vill transkribera
audio_file = "audio.wav"
# Ladda in ljudfilen
sound = AudioSegment.from_wav(audio_file)

# Definiera starttid och sluttid för det avsnitt av låten du vill transkribera (i millisekunder)
start_time_ms = 60000  # Till exempel, 1 minut in i låten
end_time_ms = 62000   # Till exempel, 2 minuter in i låten

# Extrahera det önskade avsnittet av ljudet
desired_segment = sound[start_time_ms:end_time_ms]

# Spara det önskade avsnittet av ljudet till en ny fil
desired_segment.export("desired_segment.wav", format="wav")


# Konvertera avsnittet till rå ljuddata
audio_content = desired_segment.raw_data

# Ange språket för ljudfilen, till exempel "sv-SE" för svenska
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US"
)

# Skapa en Recognize-request för det avsnittet av ljudet
audio = speech.RecognitionAudio(content=audio_content)

# Anropa Google Speech-to-Text API för att transkribera ljudet
try:
    response = client.recognize(config=config, audio=audio)
except Exception as e:
    print(f"Kunde inte transkribera det önskade avsnittet av låten: {e}")
    exit()

# Hämta transkriptionen från svaret
transcription = ""
for result in response.results:
    transcription += result.alternatives[0].transcript + " "

# Skriv ut den slutliga transkriptionen
print("Slutlig transkription:")
print(transcription)

