import requests
import json

response = requests.get("https://api.datamuse.com/words?rel_trg=random")
words = [word["word"] for word in response.json()[:10]]
# print(words)  # Output: ['chance', 'unexpected', 'luck', ...]

WORDS_DICT = {word: json.loads(requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').text)[0]['meanings'][0]['definitions'][0]['definition'] for word in words if requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').status_code == 200}
