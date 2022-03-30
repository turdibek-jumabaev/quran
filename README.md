![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

# 📖 Quran
Incomplete

## Example
#### Surah list
```python
from quran import Quran

obj = Quran()

print(data.get_surah_list())
```

#### Download surah audio
```python
obj.get_surah_audio(1, download=True)
```

#### Get audio link
```python
print(obj.get_surah_audio(1, link=True))
```

#### Download ayah image
```python
obj.get_quran_ayah_image(1, 1, download=True)
```

#### Get image link
```python
print(obj.get_quran_ayah_image(1, 1, link=True))
```

#### Get Text
```python
from quran import Text

txt = Text()
```

#### Get ayah text
```python
print(txt.get_text(1, 7, "uzbek_mansour"))
```

#### Get ayah arabic text
```python
print(txt.arabic_text(1, 7, "uzbek_mansour"))
```

#### Get sura number
```python
print(txt.sura_number(1, 7, "uzbek_mansour"))
```

#### Get aya number
```python
print(txt.aya_number(1, 7, "uzbek_mansour"))
```

#### Get ayah id
```python
print(txt.id(1, 7, "uzbek_mansour"))
```

# 🎵 Listen Quran - https://www.listen-quran.cf/
