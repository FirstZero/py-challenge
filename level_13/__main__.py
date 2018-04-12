from xmlrpc.client import ServerProxy


# Clues:
# The image shows a telephone with a text on it: "phone that evil".
# The image clickable and takes us to what looks like an xml-rpc endpoint.
# Thinking back on the last level, there was that one page saying "Bert is the evil"
# So I think what I am supposed to do is, make an RPC call to phone that evil person
# and it will give me a clue or solution maybe?
# First lets find out what methods this xml-rpc endpoint offers, if we get access (system.listMethods)

def main():
    proxy = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

    # Bullseye, the server provides a phone method!
    print(proxy.system.listMethods())

    # Lets phone the evil: Bert
    # 555-ITALY // success -> the actual anser is italy
    print(proxy.phone('Bert'))


if __name__ == '__main__':
    main()
