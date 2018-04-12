import pickle


def main():
    f = open('banner.p', mode='rb')
    data = pickle.load(f)

    for line in data:
        print(''.join(k*v for k, v in line))


if __name__ == '__main__':
    main()
