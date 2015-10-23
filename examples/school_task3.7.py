# Добавьте возможность удаления всех учителей из указанной школы

import json

with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass

school = "12 гимназия"

for el in teachers:
    if school in el["school"]:
        el.clear()
        teachers.remove(el)

with open('Teachers_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
pass
