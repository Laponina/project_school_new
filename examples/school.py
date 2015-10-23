# Имена всех учеников
# Имена всех преподавателей
# Имена и Фамилии всех учеников, учащихся в указанном классе (должна быть возможность указывать любой класс)
# Список всех школ
# * Всех учеников однофамильцев
#

import json
with open('Teachers.json', encoding='UTF-8') as f1:
    data = json.load(f1) #teachers
pass
with open('Students.json', encoding='UTF-8') as f2:
        a = json.load(f2) #students
pass

name_students = []
name_teachers = []
students_class = []
clas = '5 A'
school = []
namesake = []
surname = []

for el in data:
    name_teachers.append(el['name'])

for el in a:
    name_students.append(el['name'])
    if el['class']== "5 А":
        students_class.append(el['name']+ ' ' + el["surname"])
    if el["school"] not in school:
        school.append(el["school"])
    if el["surname"] in surname:
        namesake.append(el['surname'])
    surname.append(el["surname"])


print('Имена всех учеников:', name_students)
print('Имена всех преподавателей:', name_teachers)
print('Имена и Фамилии всех учеников, учащихся ', clas, ' классе: ', students_class)
print('Список всех школ:', school)
print('Всех учеников однофамильцев:', namesake)

# решение 3
#students_in_class = ["%s %s" % (student["name"], student["surname"])
#                     for student in students if student["class"] == class_room]