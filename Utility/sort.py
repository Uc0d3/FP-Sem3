def sort_note(students):

    sorted_students = []
    for student in students:
        if not sorted_students:
            sorted_students.append(student)
        else:
            stop = False
            for sorted_student in sorted_students:
                if student["note"] < sorted_student["note"]:
                    sorted_students.insert(sorted_students.index(sorted_student), student)
                    stop = True
                    break
            if not stop:
                sorted_students.append(student)
    return sorted_students
