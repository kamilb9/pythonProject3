from os import walk, path
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()
print(list(walk('images')))
for dir, _, files in walk('images'):
    for file in files:
        # sciezka do obrazka
        source = path.join(dir, file)
        img = Image.open(source)
        # skalowanie obrazka
        img.thumbnail((1980, 1980))
        konv = path.join(dir, 'konv_' + file.replace('.heic','.jpeg'))
        img.save(konv+'.jpeg')
