# 2➤Выведите полные имена всех учеников с указанной фамилией. Поиск нужных учеников должен осуществляться в два этапа:
# сначала ищем нужные id, потом по id выводим требуемые данные.
# Проверьте работу программы на однофамильцах.

import json

f = open('Students_id.json', 'r+', encoding='UTF-8')
students = json.load(f)
f.close()

surname = "Иванов"
id = []

for student in students:
    if student['surname'] == surname:
        id.append(student["id"])

for student in students:
    for el in id:
        if student['id'] == el:
            print(student['surname'], student['name'], student['middle_name'])