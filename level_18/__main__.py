import gzip
import difflib


def main():
    data = gzip.open('deltas.gz')

    d1 = []
    d2 = []

    for line in data:
        d1.append(line[:53].decode()+"\n")
        d2.append(line[56:].decode())

    diff = difflib.Differ().compare(d1, d2)

    f = open("f.png", "wb")
    f1 = open("f1.png", "wb")
    f2 = open("f2.png", "wb")

    for line in diff:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(' ') if o])
        if line[0] == '+':
            f1.write(bs)
        elif line[0] == '-':
            f2.write(bs)
        else:
            f.write(bs)


if __name__ == '__main__':
    main()
