from os import walk, path
from PIL import Image

print(list(walk('images')))

for dir, _, files in walk('images'):
    for file in files:
        # sciezka do obrazka
       source = path.join(dir, file)
        # otwieranie obrazka
       image=Image.open(source)
        # skalowanie obrazka
       image.thumbnail((1080, 1080))
        # tworzenie nowej nazwy dla zmniejszonych
       zmniejszone=path.join(dir, 'zmniejszony_'+file)
        # zapis zmniejszonego obrazka
       image.save(zmniejszone)