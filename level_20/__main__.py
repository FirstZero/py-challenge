import requests
import base64
import re


def main():
    cred = base64.b64encode(b'butter:fly')
    res_headers = {'Authorization': 'Basic {}'.format(cred.decode())}
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    res = requests.get(url, headers=res_headers)

    for k, v in res.headers.items():
        print('{}:\n{}\n'.format(k, v))

    while(True):
        try:
            (start, end, length) = re.search(
                r'(\d+)-(\d+)/(\d+)', res.headers['content-range']).groups()
            res_headers['range'] = 'bytes={}-'.format(int(end) + 1)
            res = requests.get(url, headers=res_headers)
            print(res.headers['content-range'])
            print(res.text)
        except KeyError:
            break

    res_headers['range'] = 'bytes={}-'.format(int(length) + 1)
    res = requests.get(url, headers=res_headers)
    (start, end, length) = re.search(
        r'(\d+)-(\d+)/(\d+)', res.headers['content-range']).groups()
    res_text = res.text
    print(res.headers['content-range'])
    print(res_text)
    print(res_text[::-1])

    res_headers['range'] = 'bytes={}-'.format(int(start) - 1)
    res = requests.get(url, headers=res_headers)
    print(res.text)

    next_level = re.search(r'and it is hiding at (\d+).', res.text).group(1)

    res_headers['range'] = 'bytes={}-'.format(next_level)
    res = requests.get(url, headers=res_headers)

    with open('../level_21/21.zip', 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    main()
