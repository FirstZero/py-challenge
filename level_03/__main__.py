import re

if __name__ == '__main__':
    data = open('data.txt').read()

    solution = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', data)
    print(solution)
    print(''.join(solution))
