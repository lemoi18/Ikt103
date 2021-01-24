word = input()

Alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

hits = [
    (Alphabet[i], word.count(Alphabet[i]))
    for i in range(26)

]

for letter, frequency in hits:
    print("'%s' : %s" % (letter.lower(), frequency))
