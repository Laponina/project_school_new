# Выведите все id учителей, преподающих в указанном классе.

import json
f = open('Teachers_id.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

form = "7 В"


for teacher in teachers:
    if form in teacher['class']:
        print(teacher['id'])