
# Clues:
# The Image is about dealing cards. The Filename is "evil1.jpg".
# Going to evil2.jpg gives us an image implying we have to get evil2.gfx instead.
# Going further to evil3.jpg gives us an image saying "no more evils". Looking
# if thats really true: evil4.jpg is not really an image. Using curl we can get "Bert is the evil"..
# No idea yet what to do with that.
# Since the image is about dealing cards into 5 stacks Im going to attempt to divide
# the data we got in the evil2.gfx to 5.


def main():
    data = open('evil2.gfx', 'rb').read()

    # lets check if its actually dividable by 5?
    print(len(data))  # 67575 - perfect

    for i in range(5):
        open('{}.jpg'.format(i), 'wb').write(
            data[i::5])  # dis - pro - port - ional - ity
    # the text in 4.jpg is actually overlined so that makes it "disproportional"


if __name__ == '__main__':
    main()
