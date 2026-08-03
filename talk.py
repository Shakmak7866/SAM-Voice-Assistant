import sounddevice as sd
import numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig

model_path = "en_US-arctic-medium.onnx"
config_path = "en_US-arctic-medium.onnx.json"

voice = PiperVoice.load(model_path, config_path=config_path)

text = "Hello! My name is Arctic from the Piper Voice API. I was built by peter pan"

syn_config = SynthesisConfig(
    length_scale = 0.7,
    speaker_id=6 # 5 6 8 16
)

for chunk in voice.synthesize(text, syn_config=syn_config):
    audio = np.frombuffer(
        chunk.audio_int16_bytes,
        dtype=np.int16
    )
    sd.play(audio, voice.config.sample_rate)
    sd.wait()

print("Audio Complete")
