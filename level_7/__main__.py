from PIL import Image
import re


def main():
    img = Image.open('oxygen.png')
    print('Height: %s' % img.height)
    print('Width: %s\n' % img.width)

    row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
    row = row[::7]

    ords = [r for r, g, b, a in row if r == g == b]

    print(''.join(map(chr, ords)))

    nums = re.findall('\d+', "".join(map(chr, ords)))
    print(''.join(map(chr, map(int, nums))))


if __name__ == '__main__':
    main()
