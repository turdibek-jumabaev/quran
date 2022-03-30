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

    def get_surah_list(self, language: str = 'en'):
        url = self.base_url + 'surah'
        params = {'language': f'{language}'}
        headers = {'Authorization': self.api_key}
        response = requests.get(url, params=params, headers=headers)
        return response.json()['data']

    def get_surah_audio(self, number, download: bool = False, link: bool = False):
        """
        {surah} - A surah number (from 1 to 114) \n
        {ayah} - An ayah number relative to the surah

        """
        if download:
            open(f"surah{number}.mp3", "wb").write(requests.get(
                f'http://server8.mp3quran.net/afs/00{number}.mp3', allow_redirects=True).content)
        if link:
            if number < 10:
                return f'http://server8.mp3quran.net/afs/00{number}.mp3'
            elif number < 100:
                return f'http://server8.mp3quran.net/afs/0{number}.mp3'
            elif number <= 114:
                return f'http://server8.mp3quran.net/afs/{number}.mp3'

        else:
            return None

    def get_quran_ayah_image(self, surah, ayah, download: bool = False, link: bool = False):
        """
        {surah} - A surah number (from 1 to 114) \n
        {ayah} - An ayah number relative to the surah

        """
        if link:
            return f"https://cdn.islamic.network/quran/images/{surah}_{ayah}.png"
        if download:
            open(f"image_{surah}_{ayah}.png", "wb").write(requests.get(
                f'https://cdn.islamic.network/quran/images/{surah}_{ayah}.png', allow_redirects=True).content)
        else:
            return None
