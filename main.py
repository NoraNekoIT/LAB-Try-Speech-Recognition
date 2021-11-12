import speech_recognition as sr

version = sr.__version__
# print(version)

r = sr.Recognizer()
# r.recognize_google()

harvard = sr.AudioFile('audio/OSR_us_000_0010_8k.wav')
# with harvard as source:
#     audio = r.record(source)
#
# print(type(audio))
#
# print(r.recognize_google(audio))

# with harvard as source:
#     audio = r.record(source, duration=2)
# print(r.recognize_google(audio))

# with harvard as source:
#
#     audio1 = r.record(source, duration=4)
#     audio2 = r.record(source, duration=4)
#
# print(r.recognize_google(audio1))
# print(r.recognize_google(audio2))

# with harvard as source:
#     audio = r.record(source, offset=4, duration=3)
#
# print(r.recognize_google(audio))

# with harvard as source:
#     audio = r.record(source, offset=4.7, duration=2.8)
#
# print(r.recognize_google(audio))


jackhammer = sr.AudioFile('audio/audio_files_jackhammer.wav')
# with jackhammer as source1:
#     audio1 = r.record(source1)
#
# print(r.recognize_google(audio1))
#
# with jackhammer as source2:
#     r.adjust_for_ambient_noise(source2)
#     audio2 = r.record(source2)
#
# print(r.recognize_google(audio2))
#
# with jackhammer as source3:
#     r.adjust_for_ambient_noise(source3, duration=0.5)
#     audio3 = r.record(source3)
#
# print(r.recognize_google(audio3))

with jackhammer as source4:
    r.adjust_for_ambient_noise(source4, duration=0.5)
    audio4 = r.record(source4)
print(r.recognize_google(audio4, show_all=True))