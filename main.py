from UI.ui import read_student, print_menu
from Repository.adauga import adauga
from Utility.sort import sort_students, sort_alpha_note


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
    {
        "id": 3,
        "name": "Aaa",
        "note": 6
    },
]

while True:
    try:
        print_menu()
        op = int(input("Options:"))
        if op == 1:
            student = read_student(students)
            adauga(students, student)
            print (students)
        if op == 2:
            sorted_students = sort_students(students, "note")
            print("Sorted:")
            print(sorted_students)
        if op == 3:
            sorted_students = sort_alpha_note(students)
            print("Sorted:")
            print(sorted_students)
    except Exception as e:
        print(e)
