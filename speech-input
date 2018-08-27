import speech_recognition as sr
import pyperclip
import pyautogui

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

pyperclip.copy(r.recognize_google(audio, language='ja-JP'))
pyautogui.hotkey('ctrl', 'V')
