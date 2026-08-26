"""PyAudio Example: Play a wave file."""

import wave
import sys
import pyaudio
import numpy as np


CHUNK = 1024
RATE = 44100
FORMAT = pyaudio.paInt16
THRESHOLD = 500

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, 
                channels=1, 
                rate=RATE, 
                input=True, 
                frames_per_buffer=CHUNK)

player = p.open(format=FORMAT, 
                channels=1, 
                rate=RATE, 
                output=True, 
                frames_per_buffer=CHUNK)

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
except KeyboardInterrupt:
    print("Stopping")



stream.stop_stream()
stream.close()
p.terminate()
