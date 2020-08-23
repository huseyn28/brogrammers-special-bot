import requests

from constants import MEME_API_URL
from interceptors import logger_interceptor


@logger_interceptor
def get_random_meme():
    return requests.get(MEME_API_URL,headers={'User-Agent': 'Chrome'}).json()

