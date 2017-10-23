def read_student(students):
    id = len(students) + 1
    name = input("Name:")
    nota = int(input("Nota:"))

    student = {
        "id": id,
        "name": name,
        "note": nota
    }
    return student


def print_menu():
    options = """
    1 - Add student
    2 - Sort Students by note
    3 - Sort name where note > 5
    """
    print(options)
