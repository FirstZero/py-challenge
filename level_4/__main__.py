import re
import requests

# Entry point: 12345


def get_next_nothing(num):
    pattern = re.compile('and the next nothing is ([0-9]+)')

    while True:
        r = requests.get(
            'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % num)
        m = pattern.search(r.text)
        print(r.text)
        if m == None:
            break
        num = m.group(1)
    return num


def main():
    next_nothing = '12345'
    next_nothing = get_next_nothing(next_nothing)
    next_nothing = str(int(next_nothing) / 2)
    get_next_nothing(next_nothing)


if __name__ == '__main__':
    main()
