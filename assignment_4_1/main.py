import json
import math

from school import *

with open('students.json') as json_file:
    root = json.load(json_file)
    count = 0
    n = 0
    data = {}
    low_age = []
    attend = {}
    for students in root:
        student = Student(students['id'], students['name'], students['age'], students['attendance'])
        count +=1
        n += student.age
        print(student.age)
        if student.age not in low_age:
            low_age.append(student.age)

        if student.name and student.attendance not in attend:
            attend[student.name] = student.attendance

        if student.name and student.age not in data:
            data[student.name] = student.age

    for name, age in data.items():
        if age == min(low_age):
            print(f'Youngest: {name}')

    for name, age in data.items():
        if age == max(low_age):
            print(f'Oldest: {name}')
    print(n,count)
    average = n / count
    print(f'Average age: { math.floor(average)}')

    for name, attendance in attend.items():
        if attendance < 30:
            print(f'Bad student: {name}')

    pass
