import requests
from funksjoner import *

print('1. Read all students')
print('2. Get student by id')
print('3. Add student')
print('4. Edit student')
print('5. Remove student')
print('6. Exit')

x = 1
while x == 1:
    choice = input()
    if choice == '1':
        read()

    elif choice == '2':
        readid(int(input()))

    elif choice == '3':
        name= input()
        email=input()
        year= int((input()))
        add_student(name, email, year)

    elif choice == '4':

        edit_student(int(input()), input(), input(), int(input()))

    elif choice == '5':
        delete_student(int(input()))

    elif choice == '6':
        x = 0
