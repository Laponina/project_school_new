# Добавьте возможность удалять указанные классы у указанного преподавателя
import json

with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass

form = "9 А"
name = 'Иванов Георгий Константинович'

for teacher in teachers:
    if "%s %s %s" % (teacher["surname"], teacher["name"], teacher["middle_name"]) == name:
        for el in teacher['class']:
            if form ==el:
                teacher['class'].remove(el)

with open('Teachers_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
pass