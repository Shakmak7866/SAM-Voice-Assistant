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
