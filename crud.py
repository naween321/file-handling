from create import create
from read import read
from update import update
from delete import delete


def inquiry():
    selection = input("Welcome to Broadway. Choose C/R/U/D/E ")
    selection = selection.lower()

    def continue_or_not(c):
        inquiry() if c else print("Thank you see you again")

    if selection == 'c':
        cont = create()
        return continue_or_not(cont)
        # if cont:
        #     inquiry()
        # else:
        #     print("Thank You. See you again")
    elif selection == 'r':
        id = input("Enter the student ID ")
        cont = read(id)
        return continue_or_not(cont)
    elif selection == 'u':
        cont = update()
        return continue_or_not(cont)

    elif selection == 'd':
        cont = delete()
        return continue_or_not(cont)
    else:
        print("Thank You. See you again")


inquiry()
