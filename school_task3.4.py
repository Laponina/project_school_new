# Добавьте возможность удаления ученика по заданному полному имени

import json

f = open('Students.json', 'r+', encoding='UTF-8')
students = json.load(f)

f.close()

student = 'Красный Василий'


for el in students:
    if "%s %s" % (el["surname"], el["name"]) == student:
        el.clear()
        students.remove(el)



f = open('Students.json', 'w', encoding='UTF-8')
f.write(json.dumps(students, ensure_ascii=False)+'\n')

f.close()
