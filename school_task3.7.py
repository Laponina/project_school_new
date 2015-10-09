#Добавьте возможность удаления всех учителей из указанной школы

import json

f = open ('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

school = "12 гимназия"

for el in teachers:
    if school in el["school"]:
        el.clear()
        teachers.remove(el)

f = open ('Teachers.json', 'w', encoding='UTF-8')
f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
f.close()