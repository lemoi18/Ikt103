count = 0
n = 0
s = set()
word = input()
words = []
while word != 'stop':
    s.add(word)
    word = input()
    words.append(word)
    n += 1
    

for word in s:
    count += 1

print('Total :', n)
print('Unique :', count)


def count(elementer):
    if elementer in dictionary:
        dictionary[elementer] += 1

    else:
        dictionary.update({elementer: 1})


dictionary = {}

for elements in words:
    count(elements)

# print the keys and its corresponding values.
for allKeys in dictionary:
    print(allKeys, end=" ")
    print(":", end=" ")
    print(dictionary[allKeys], end=" ")
    print()
