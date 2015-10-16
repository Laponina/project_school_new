#Полные имена (full_name) всех учеников для указанного учителя


import json

with open('Teachers_id.json', encoding='UTF-8') as f1:
    teachers = json.load(f1)
pass
with open('Students_id.json', encoding='UTF-8') as f2:
    students = json.load(f2)
pass

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