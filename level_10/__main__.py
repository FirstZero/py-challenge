from itertools import groupby, islice


def look_and_say(number='1'):
    while True:
        yield number
        number = ''.join(str(len(list(g))) + k for k, g in groupby(number))


def main():
    a = [x for x in islice(look_and_say(), 31)]  # index a[30]
    print(len(a[30]))


if __name__ == '__main__':
    main()
