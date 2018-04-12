from zipfile import ZipFile
import re

# Entry point: 90052


def main():
    num = 90052
    file_comments = []

    with ZipFile('channel.zip') as zf:
        pattern = re.compile('Next nothing is ([0-9]+)')
        while True:
            zf_file = zf.read('%s.txt' % num).decode()
            m = pattern.search(zf_file)
            print(zf_file)
            file_comments.append(zf.getinfo('%s.txt' % num).comment.decode())
            if m == None:
                break
            num = m.group(1)
    print(''.join(file_comments))


if __name__ == '__main__':
    main()
