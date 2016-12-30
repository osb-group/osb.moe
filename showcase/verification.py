"""
verification.py:
--> Used to verify an account on osu! with an account on osb.moe
--> Obviously, this is only the algorithm that does this process.
"""

import os
from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADJECTIVE_PATH = os.path.join(BASE_DIR, 'hentai/adjectives.txt')
NOUN_PATH = os.path.join(BASE_DIR, 'hentai/nouns.txt')


def generate_key(username):

    def partition(lst, n):
        division = len(lst) / float(n)
        return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n)]

    def convert_string_to_key(s):
        now = timezone.now()
        date_key = now.day * (now.hour+1)
        return date_key * (sum([ord(c) for c in s]) if s else 0)

    def convert_key_to_word(key, use_nouns=False):
        with open(NOUN_PATH if use_nouns else ADJECTIVE_PATH) as f:
            lines = list(f)
            word = lines[key % len(lines)]
            return str.title(word).rstrip('\r\n')

    def convert(word, use_nouns=False):
        return convert_key_to_word(convert_string_to_key(word), use_nouns)
    partitions = partition(username, 3)
    return ''.join([convert(w) for w in partitions[:-1]]) + convert(partitions[len(partitions)-1], use_nouns=True)
