import os
import json
filename = "students.txt"


def create():
    id = input("Enter the id of student ")
    name = input("Enter name of the student ")
    dept = input("Enter the department ")
    student = dict(id=id, name=name, department=dept)
    if os.path.exists(filename):
        with open(filename, "r") as fp:
            students = fp.read()
            students = json.loads(students)
    else:
        students = []
    students.append(student)
    with open(filename, 'w') as fp:
        json.dump(students, fp)
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    return True if cont.lower() == 'y' else False
