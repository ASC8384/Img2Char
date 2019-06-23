import string

from PIL import Image

char = list(string.printable + " ")
length = len(char)

FILE = input()
IMG = Image.open(FILE)

txt = ""

for i in range(IMG.size[0]):
    for j in range(IMG.size[1]):
        r, g, b, a = IMG.getpixel((i, j))
        if a:
            grey = (r + g + b) // 3
            txt += char[int(grey * length / (256 + 1))]
        else:
            txt += ' '
    txt += '\n'

print(txt)

input()
