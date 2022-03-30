"""
        Quran APP 
        ~~~~~~~~
        This is the main module of the Quran app.

        Turdibek Jumabaev < 
        30.03.2022
"""

import requests


class Quran():

    def __init__(self):
        self.base_url = 'http://api.alquran.cloud/v1/'
        self.api_key = '8f6b8c8a-b6e7-4d2b-a8f2-e9d9b9e9a8a1'

    def get_surah_list(self):
        url = self.base_url + 'surah'
        params = {'language': 'en'}
        headers = {'Authorization': self.api_key}
        response = requests.get(url, params=params, headers=headers)
        return response.json()['data']

    def get_surah_audio(self, number, download: bool = False, link: bool = False):
        if download:
            open(f"surah{number}.mp3", "wb").write(requests.get(
                f'http://server8.mp3quran.net/afs/00{number}.mp3', allow_redirects=True))
        if link:
            if number < 10:
                return f'http://server8.mp3quran.net/afs/00{number}.mp3'
            elif number < 100:
                return f'http://server8.mp3quran.net/afs/0{number}.mp3'
            elif number <= 114:
                return f'http://server8.mp3quran.net/afs/{number}.mp3'
