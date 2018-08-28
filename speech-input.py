import speech_recognition as sr
import pyperclip
import pyautogui

def check_maruten(text):
    if text == "まる":
        return "。"
    elif text == "10":
        return "、"
    elif text == "改行":
        return "\n"
    else:
        return text

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    text = r.recognize_google(audio, language='ja-JP')
    text = check_maruten(text)

    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'V')

###################
main()
