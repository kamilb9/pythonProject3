# program do konwersji zdjec HEIC do JPEG
# autor: Kamil Basiński

from os import walk, path
from PIL import Image
import pillow_heif
import os

szerokosc=1980
wysokosc=1980

pillow_heif.register_heif_opener()
print(list(walk('images')))
for dir, _, files in walk('images'):
    for file in files:
        # sciezka do obrazka
        source = path.join(dir, file)
        img = Image.open(source)
        # skalowanie obrazka
        img.thumbnail((szerokosc, wysokosc))
        # konwersja i zmiana nazwy
        konv = path.join(dir, '_'+ str(szerokosc) +'_'+ str(wysokosc) +'_'+ file.replace('.heic','.jpeg'))
        # zapis zmienionego obrazka
        img.save(konv)

