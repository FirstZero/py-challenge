from PIL import Image, ImageDraw


def main():
    first = list()
    second = list()

    with open('first.txt') as f:
        first = [int(x) for x in f.read().split(',')]

    with open('second.txt') as f:
        second = [int(x) for x in f.read().split(',')]

    im = Image.new('RGB', (500, 500))
    draw = ImageDraw.Draw(im)

    draw.polygon(first)
    draw.polygon(second)
    im.show('result.png')


if __name__ == '__main__':
    main()
