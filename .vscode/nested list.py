num_students = int(input())


students = []


for _ in range(num_students):
    name = input()
    grade = float(input())
    students.append([name, grade])


grades = sorted(set([grade for name, grade in students]))
second_lowest_grade = grades[1]


second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]


for student in sorted(second_lowest_students):
    print(student)

        
