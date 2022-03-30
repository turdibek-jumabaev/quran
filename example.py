from quran import Text
from quran import Quran

##################################################################
### AUDIO ## IMAGE ## LINK ## AUDIO ## IMAGE ## LINK ## AUDIO ###
##################################################################

data = Quran()

""" surah list """
print(data.get_surah_list())

""" download audio """
data.get_surah_audio(1, download=True)

""" get surah audio link """
print(data.get_surah_audio(1, link=True))

""" download image"""
data.get_quran_ayah_image(1, 1, download=True)

""" get image link """
print(data.get_quran_ayah_image(1, 1, link=True))

##################################################################
## TEXT ## TEXT ## TEXT ## TEXT ## TEXT ## TEXT ## TEXT ## TEXT ##
##################################################################

txt = Text()

""" get ayah text """
print(txt.get_text(1, 7, "uzbek_mansour"))

""" get ayah arabic text """
print(txt.arabic_text(1, 7, "uzbek_mansour"))

""" get sura number """
print(txt.sura_number(1, 7, "uzbek_mansour"))

""" get aya number """
print(txt.aya_number(1, 7, "uzbek_mansour"))

""" get ayah id """
print(txt.id(1, 7, "uzbek_mansour"))
