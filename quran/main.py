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
