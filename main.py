from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="google/gemma-2-2b-it")
print(pipe(messages))