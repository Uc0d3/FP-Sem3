from UI.ui import read_student, print_menu
from Repository.adauga import adauga
from Utility.sort import sort_note


students = [
    {
        "id": 1,
        "name": "test",
        "note": 8
    },
    {
        "id": 2,
        "name": "Vic",
        "note": 10
    },
    {
        "id": 3,
        "name": "Rob",
        "note": 1
    },
]

while True:
    print_menu()
    op = int(input("Options:"))
    if op == 1:
        student = read_student(students)
        adauga(students, student)
        print (students)
    if op == 2:
        sorted_students = sort_note(students)
        print("Sorted:")
        print(sorted_students)
