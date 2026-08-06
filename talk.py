import sounddevice as sd
import numpy as np
from kokoro_onnx import Kokoro

model_path = "kokoro-v1.0.onnx"
voices_path = "voices-v1.0.bin"

kokoro = Kokoro(model_path, voices_path)

text = "Hello! My name is Sam from the Kokoro Voice API. I am your personal Voice Assistant."

audio, sample_rate = kokoro.create(
    text=text,
    voice="af_heart",
)

sd.play(audio, sample_rate)
sd.wait()


text = "How shall I help you today?!"

audio, sample_rate = kokoro.create(
    text=text,
    voice="af_heart",
)

sd.play(audio, sample_rate)
sd.wait()

print("Audio Complete")
