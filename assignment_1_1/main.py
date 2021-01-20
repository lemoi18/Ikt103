count = 1

for i in range(10):
    print(count, end=' ')
    count += 1

print("\n")
count = 1
for i in range(10):
    print(count, end=' ')
    count += 2

print("\n")
count = 2
for i in range(10):
    print(count, end=' ')
    count += 2

print("\n")
count = 1
for i in range(17):
    print(count, end=' ')
    count += 3

print("\n")
count = 40
for i in range(10):
    print(count, end=' ')
    count -= 4

print("\n")

for count in range(100):
    if count > 1:
        for i in range(2, count):
            if (count % i) == 0:
                break
        else:
            print(count, end=' ')
