# Добавьте возможность удалять указанные классы у указанного преподавателя
import json

f = open('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

form = "9 А"
name = 'Иванов Георгий Константинович'

for teacher in teachers:
    if "%s %s %s" % (teacher["surname"], teacher["name"], teacher["middle_name"]) == name:
        for el in teacher['class']:
            if form ==el:
                teacher['class'].remove(el)

f = open('Teachers.json', 'w', encoding='UTF-8')

f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
f.close()