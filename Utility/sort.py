def sort_students(students, key):
        sorted_students = []
        for student in students:
            if not sorted_students:
                sorted_students.append(student)
            else:
                stop = False
                for sorted_student in sorted_students:
                    if student[key] < sorted_student[key]:
                        sorted_students.insert(sorted_students.index(sorted_student), student)
                        stop = True
                        break
                if not stop:
                    sorted_students.append(student)
        return sorted_students


def sort_alpha_note(students):
    fitred = [student for student in students if student["note"] > 5]
    return (sort_students(fitred, "name"))
