import requests

from constants import MEME_API_URL


def get_random_meme():
    return requests.get(MEME_API_URL,headers={'User-Agent': 'Chrome'}).json()

