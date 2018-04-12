import requests
import re
import bz2
import urllib.parse
import xmlrpc.client


def main():
    num = '12345'
    info = ''
    while(True):
        res = requests.get(
            'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(num))
        print(res.text)
        info += res.cookies['info']
        match = re.search('and the next busynothing is (\d+)', res.text)
        if match == None:
            break
        else:
            num = match.group(1)
    info = urllib.parse.unquote_to_bytes(info.replace('+', ' '))
    info = bz2.decompress(info)

    print(info)

    proxy = xmlrpc.client.ServerProxy(
        'http://www.pythonchallenge.com/pc/phonebook.php')
    print(proxy.phone('Leopold'))

    message = 'the flowers are on their way'

    req_cookies = {'info': urllib.parse.quote_plus(message)}
    res = requests.get(
        'http://www.pythonchallenge.com/pc/stuff/violin.php', cookies=req_cookies)
    print(res.text)


if __name__ == '__main__':
    main()
