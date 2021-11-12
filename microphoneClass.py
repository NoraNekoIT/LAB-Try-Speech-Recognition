import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

print(sr.Microphone.list_microphone_names())

# # This is just an example; do not run
# mic = sr.Microphone(device_index=3)

# with mic as source:
#     audio = r.listen(source)
#
# print(r.recognize_google(audio))

# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# print(r.recognize_google(audio))

