palavra = input(': ').lower()
leet = {
    'a': '4',
    'b': '|3',
    'c': '<',
    'd': '|>',
    'e': '3',
    'f': '|=',
    'g': '(,',
    'h': '|-|',
    'i': '!',
    'j': 'j',
    'k': '|<',
    'l': '1',
    'm': '|v|',
    'n': '|\|',
    'o': '0',
    'p': '|°',
    'q': 'q',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': '`/',
    'z': '2'
}

for key in leet.keys():
    palavra = palavra.replace(key, leet[key])

print(palavra)