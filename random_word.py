import random
import dict_word

WORDS_DICT = dict_word.WORDS_DICT

def get_word():
    return random.choice(list(WORDS_DICT.items()))