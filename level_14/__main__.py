from PIL import Image


def main():
    im = Image.open('wire.png')
    print(im.size)  # (10000, 1) <- x,y

    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    result_image = Image.new('RGB', (100, 100))

    x, y, p = -1, 0, 0

    d = 200

    while d / 2 > 0:
        for v in delta:
            steps = d // 2
            for _ in range(steps):
                x = x + v[0]
                y = y + v[1]

                result_image.putpixel((x, y), im.getpixel((p, 0)))
                p += 1
            d -= 1
    result_image.show()


if __name__ == '__main__':
    main()
