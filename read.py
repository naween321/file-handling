from estd_connection import estd_connection


def read(id):
    cursor = estd_connection()
    sql = f"""
    SELECT * FROM STUDENT WHERE ID='{id}'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cont = input("Do you want to continue? (y/n)")
    return cont.lower() == 'y'




# def read(id):
#     with open(filename, 'r') as fp:
#         students = json.load(fp)
#     student = list(filter(lambda x: x['id']==id, students))
#     print(student[0])
#     cont = input("Do you want to continue? (y/n)")
#     return True if cont.lower() == 'y' else False
