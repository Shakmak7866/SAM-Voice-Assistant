import os
import sys
import speech_recognition as sr
import subprocess
import platform

#open_terminal():
#   subprocess.run(["ls"])

stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

p = pyaudio.pyAudio()

sys.stderr = stderr

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source, 10, 3)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        if "terminal" in text:
            #p = subprocess.Popen(["alacritty"])
            p = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate("ls")
            p.stdin.write(b"ls")
            p.stdin.flush()
            print("Output:", stdout.decode())
        #open_terminal()
        if "please" in text:
            break
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print(e)

print(hello)
sys.stderr = stderr
