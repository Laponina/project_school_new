# Выведите все id учителей, преподающих в указанном классе.

import json
with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass

form = "7 В"


for teacher in teachers:
    if form in teacher['class']:
        print(teacher['id'])