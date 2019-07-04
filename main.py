import string

from PIL import Image

# 导入可打印字符集，并保证最后一位为空
char = list(string.printable + " ")
length = len(char)

# 输入目标路径
FILE = input()
IMG = Image.open(FILE)

txt = ""

# 遍历图片行、列
for i in range(IMG.size[0]):
    for j in range(IMG.size[1]):
        # 取出像素点的 R、G、B、alpha 值
        r, g, b, a = IMG.getpixel((i, j))
        # 判断是否透明
        if a:
            # 灰度值公式
            grey = (r + g + b) // 3
            # 灰度映射到字符集
            txt += char[int(grey * length / (256 + 1))]
        else:
            txt += ' '
    txt += '\n'

print(txt)

input()
