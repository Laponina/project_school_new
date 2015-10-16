#Полное имя учителя для указанного ученика(ученика указываем по Имя + Фамилия). Что делать, если есть однофамильцы с одинаковыми именами?
import json

with open('Teachers_id.json', encoding='UTF-8') as f1:
    teachers = json.load(f1)
pass
with open('Students_id.json', encoding='UTF-8') as f2:
    students = json.load(f2)
pass

student_name = 'Матвей Петров'
teacher_of = []
class_rooms = []
school_num = -1

for el in students:
    if "%s %s" % (el["name"], el["surname"]) == student_name:
        class_rooms = el["class"]
        school_num = el["school"]

for el in teachers:
    if (class_rooms in el['class']) and (school_num == el["school"]):
        teacher_of.append("%s %s %s" % (el["name"], el["middle_name"], el["surname"]))


if not teacher_of:
    print('Данного учителя нет')
else:
    print('Полное имя учителя для указанного ученика:', teacher_of)
