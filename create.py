from estd_connection import estd_connection


def create():
    cursor = estd_connection()
    id = input("Enter the id of student ")
    name = input("Enter name of the student ")
    dept = input("Enter the department ")
    sql = f"""
        INSERT INTO STUDENT(ID, NAME, DEPARTMENT)
        VALUES ('{id}', '{name}', '{dept}')
        """
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    cursor.execute(sql)
    return cont.lower() == 'y'





#def create():
    # id = input("Enter the id of student ")
    # name = input("Enter name of the student ")
    # dept = input("Enter the department ")
    # student = dict(id=id, name=name, department=dept)
    # if os.path.exists(filename):
    #     with open(filename, "r") as fp:
    #         students = json.load(fp)
    # else:
    #     students = []
    # students.append(student)
    # with open(filename, 'w') as fp:
    #     json.dump(students, fp, indent=2)
    # cont = input("A new student has been added. Do you want to continue? (y/n)")
    # return True if cont.lower() == 'y' else False
