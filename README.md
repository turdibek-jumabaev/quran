# quran
Incomplete

## Example
#### Surah list
```python
from quran import Quran

data = Quran()

print(data.get_surah_list())
```

#### Download surah audio
```python
data.get_surah_audio(1, download=True)
```

#### Get audio link
```python
print(data.get_surah_audio(1, link=True))
```
