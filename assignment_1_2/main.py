

words = input()

print(len(words))

def Palindrome(s):
    return s == s[::-1]

answer = Palindrome(words)
if answer:
    print("is a palindrome")
else:
    print("is not a palindrome")

print(words[::-1])
