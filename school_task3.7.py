#Добавьте возможность удаления всех учителей из указанной школы

import json

f = open ('Teacher.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

form = "12 гимназия"

for el in teachers:
    if form in el['class']:
        el.clear()
        teachers.remove()
