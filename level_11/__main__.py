from PIL import Image


# Clues:
# There arent really much clues, except the title of the page saying "odd even".
# Most likely it implies we have to split the image into odd/even

def main():
    im = Image.open('cave.jpg')
    (w, h) = im.size

    odd = Image.new('RGB', (w // 2, h // 2))
    even = Image.new('RGB', (w // 2, h // 2))

    for i in range(w):
        for j in range(h):
            p = im.getpixel((i, j))
            if (i+j) % 2 == 1:
                odd.putpixel((i // 2, j // 2), p)
            else:
                even.putpixel((i // 2, j // 2), p)

    odd.save('odd.jpg')
    even.save('even.jpg')


if __name__ == '__main__':
    main()
