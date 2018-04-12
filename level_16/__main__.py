from PIL import Image
import numpy as np


def main():
    im = Image.open('mozart.gif')
    im.show()
    # most pixels (60)
    print(max(enumerate(im.histogram()), key=lambda x: x[1]))

    print([x for x in enumerate(im.histogram())
           if x[1] % im.height == 0 and x[1] != 0])  # pixels dividable by height (2400)

    tmp_im = im.copy()
    tmp_im.frombytes(bytes([195] * (tmp_im.width * tmp_im.height))).show()

    shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist())
               for row in np.array(im)]

    Image.frombytes(im.mode, im.size, b''.join(shifted)).show()


if __name__ == '__main__':
    main()
