from estd_connection import estd_connection


def update(id, to_change, value):
    cursor = estd_connection()
    sql = f"""
    UPDATE STUDENT SET {to_change.upper()}='{value}' WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been updated. Do you want to continue? (y/n)")
    return cont.lower() == 'y'


# def update(id, to_change, value):
#     with open(filename, 'r') as fp:
#         students = json.load(fp)
#     student = list(filter(lambda x: x['id'] == id, students))[0]
#     # [{"id": 2, "name": "Ram", "department": "Elex"}]
#     # student = student[0]
#     index_of_student = students.index(student)
#     students[index_of_student][to_change] = value
#     with open(filename, 'w') as fp:
#         json.dump(students, fp, indent=2)
#     cont = input("The student has been updated. Do you want to continue? (y/n)")
#     return True if cont.lower() == 'y' else False

# Add Comment
