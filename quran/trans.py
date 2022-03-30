import requests


class Text():

    def __init__(self):
        url = "https://quranenc.com/api/v1/translations/list"

    def translation_list(self):
        return requests.get("https://quranenc.com/api/v1/translations/list").json()["translations"]

    def get_keys(self):
        result = []
        for i in range(0, len(self.translation_list())):
            result.append({self.translation_list()[
                          i]['language_iso_code']: self.translation_list()[i]['key']})
        return result

    def get_text(self, surah: int, ayah: int, key: str):
        return requests.get(f"https://quranenc.com/api/v1/translation/aya/{key}/{surah}/{ayah}").json()["result"]

    def translaton(self, surah, ayah, key):
        return self.get_text(surah, ayah, key)["translation"]

    def arabic_text(self, surah, ayah, key):
        return self.get_text(surah, ayah, key)["arabic_text"]

    def sura_number(self, surah, ayah, key):
        return self.get_text(surah, ayah, key)["sura"]

    def aya_number(self, surah, ayah, key):
        return self.get_text(surah, ayah, key)["aya"]

    def id(self, surah, ayah, key):
        return self.get_text(surah, ayah, key)["id"]
