import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('audio/meAudio.wav') as source:
    audio = r.record(source)

print(r.recognize_google(audio, language='id-ID'))
