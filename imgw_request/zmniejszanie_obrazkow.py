from os import walk, path

print(list(walk('images')))

for dir, _, files in walk('images'):
    for file in files:
        print(path.join(dir, file))