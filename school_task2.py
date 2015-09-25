#Полные имена (full_name) всех учеников для указанного учителя


import json

f1 = open('Teachers.json', encoding='UTF-8')
f2 = open('Students.json', encoding='UTF-8')

teachers = json.load(f1)
students = json.load(f2)

teacher = 'Владимир Сергеевич'
students_of = []
class_rooms = []
school_num = -1

for el in teachers:
    if "%s %s" % (el["name"], el["middle_name"]) == teacher:
        class_rooms = el["class"]
        school_num = el["school"]

for el in students:
    if (el['class'] in class_rooms) and (school_num == el["school"]):
        students_of.append("%s %s %s" % (el["name"], el["middle_name"], el["surname"]))

if not class_rooms:
    print('Данного учителя нет')
else:
    print('Полные имена всех учеников для указанного учителя:', students_of)