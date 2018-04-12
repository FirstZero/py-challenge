if __name__ == '__main__':
    data = open('data.txt').read()

    count = {}

    for c in data:
        count[c] = count.get(c, 0) + 1

    for k, v in count.items():
        if v == 1:
            print(k, end='')
