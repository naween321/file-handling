from estd_connection import estd_connection


def delete(id):
    cursor = estd_connection()
    sql = f"""
    DELETE FROM STUDENT WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been deleted. Do you want to continue? (y/n)")
    return cont.lower() == 'y'




# def delete(id):
#     with open(filename, 'r') as fp:
#         students = json.load(fp)
#     student = list(filter(lambda x: x['id'] == id, students))[0]
#     students.remove(student)
#     with open(filename, 'w') as fp:
#         json.dump(students, fp, indent=2)
#     cont = input("The student has been deleted. Do you want to continue? (y/n)")
#     return True if cont.lower() == 'y' else False
