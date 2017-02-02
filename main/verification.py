"""
verification.py:
--> Used to verify an account on osu! with an account on osb.moe
--> Obviously, this is only the algorithm that does this process.
"""

import os
import json
import requests
from django.shortcuts import render
from django.utils import timezone

from .forms import OsuUserVerificationForm

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


def is_match_name_correct(match_output, username):
    try:
        match = match_output["match"]
        return match["name"] == generate_key(username)
    except:
        return False


def fetch_match(match_id):
    # Code here uses requests python library to make query to osu!api
    # Use hifumi secret to load the osu! api key
    # Return the json list
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HIFUMI_PATH = os.path.join(BASE_DIR, 'hentai/hifumi.json')

    # Load exterior .json file
    try:
        with open(HIFUMI_PATH) as handle:
            OUTSIDE_INFO = json.load(handle)
    except IOError:
        raise
    api_key = OUTSIDE_INFO["osu_api_key"]

    # Build the osu! API url with the given information
    osu_url = r'https://osu.ppy.sh/api/get_match?k={0}&mp={1}'.format(api_key,match_id)
    request = requests.get(osu_url)
    return request.json()


def send_validation(request):
    # From a form for validation
    if request.method == "POST":
        form = OsuUserVerificationForm(request.POST)
        if form.is_valid():
            match_id = form.cleaned_data['match_id']
            osu_username = form.cleaned_data['osu_username']
            if match_id == 0:
                # Just generating first...
                return render(request, 'user/verification_form.html', {'form': form, 'is_submitted': False, 'verification_code':generate_key(osu_username)} )
            match_json = fetch_match(match_id)
            if is_match_name_correct(match_json, osu_username):
                # Get the user account
                # Get the corresponding storyboarder with that osu_username, if one exists
                # Something...
                raise NotImplementedError
            else:
                # Incorrect match
                return render(request, 'user/verification_form.html', {'form': form, 'is_submitted': True, 'verification_code':generate_key(osu_username)} )
    else:
        # This is the initial validation form.
        form = OsuUserVerificationForm()
        return render(request, 'user/verification_form.html', {'form': form, 'is_submitted': False} )