
s = input()
for i in range(len(s)):
    b = s.count(s[i])
    print("'{}' : {}".format(s[i], b))
