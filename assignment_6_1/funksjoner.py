import requests
import json

def read():
    result = requests.get('http://localhost:5000/students/')

    students = result.json()
    for users in students:
        print(f'id: {users["id"]}, name: {users["name"]}, email: {users["email"]}, year: {users["year"]}')


def readid(i):
    result2 = requests.get(f'http://localhost:5000/students/{i}')

    user = result2.json()

    if result2.status_code == 200:
        print(f'{result2.status_code} OK')
        print(f'id: {user["id"]}, name: {user["name"]}, email: {user["email"]}, year: {user["year"]}')
    else:
        print(f'{result2.status_code} Not Found')
        print('Student not found')


def add_student(x, y, z):
    comment = dict(id=len(requests.get('http://localhost:5000/students/').json()) + 1, name=str(x),
                   email=str(y), year=int(z))
    new_student = requests.post('http://localhost:5000/students/', json=comment)
    print(
        f'Added student: id: {comment["id"]}, name: {comment["name"]}, email: {comment["email"]}, year: {comment["year"]}')


def edit_student(v, y, z, w):
    comment = dict(id=int(v), name=str(y), email=str(z), year=int(w))
    edit_students = requests.put(f'http://localhost:5000/students/{v}', json=comment)
    if edit_students.status_code == 200:
        print("Student was edited successfully")
    elif edit_students.status_code == 404:
        print("Student not found")
    else:
        print(f"Request failed with status code {edit_students.status_code}")


def delete_student(d):
    delete_student = requests.delete(f'http://localhost:5000/students/{d}')

    if delete_student.status_code == 204:
        print("Student was removed successfully")
    if delete_student.status_code == 404:
        print("Student not found")
    else:
        return
