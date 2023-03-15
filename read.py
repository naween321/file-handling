import json
filename = "students.txt"


def read(id):
    with open(filename, 'r') as fp:
        students = fp.read()
        students = json.loads(students)
    student = list(filter(lambda x: x['id']==id, students))
    print(student[0])
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    return True if cont.lower() == 'y' else False
