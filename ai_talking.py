import sounddevice as sd
import numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig
from ollama import chat
from ollama import ChatResponse


response: ChatResponse = chat(
    model = 'gemma3:1b',
    messages=[
        {
            'role': 'user',
            'content': 'Hello! Tell me a one-sentence fun fact about python',
        },
    ]
)

print(response['message']['content'])
text = response['message']['content']

model_path = "en_US-arctic-medium.onnx"
config_path = "en_US-arctic-medium.onnx.json"

voice = PiperVoice.load(model_path, config_path=config_path)

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

