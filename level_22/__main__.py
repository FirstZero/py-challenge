from PIL import Image, ImageDraw


def main():
    im = Image.open('white.gif')
    new_im = Image.new('RGB', (500, 200))

    draw = ImageDraw.Draw(new_im)

    cx = 0
    cy = 100

    for frame in range(im.n_frames):
        im.seek(frame)
        left, top = im.getbbox()

        dx = left - 100
        dy = top - 100

        if dx == dy == 0:
            cx += 50
            cy = 100
        cx += dx
        cy += dy

        draw.point((cx, cy))
    new_im.show()


if __name__ == '__main__':
    main()
