import requests
import json


response = requests.get("https://api.datamuse.com/words?rel_trg=random")

"""[
    {"word": "chance", "score": 1000},
    {"word": "unexpected", "score": 950},
    {"word": "luck", "score": 900},
    ...
]"""



words = [word["word"] for word in response.json()[:10]] # print(words)  # Output: ['chance', 'unexpected', 'luck', ...]

WORDS_DICT = {word: json.loads(requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').text)[0]['meanings'][0]['definitions'][0]['definition'] for word in words if requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').status_code == 200}
"""
[
    {
        "word": "chance",
        "phonetics": [
            {
                "text": "/tʃæns/",
                "audio": "https://audio.oxforddictionaries.com/en/mp3/chance_us_1.mp3"
            }
        ],
        "meanings": [
            {
                "partOfSpeech": "noun",
                "definitions": [
                    {
                        "definition": "A possibility of something happening.",
                        "example": "there is a chance of winning the lottery",
                        "synonyms": ["possibility", "likelihood"],
                        "antonyms": ["certainty"]
                    }
                ]
            }
        ]
    }
]
"""