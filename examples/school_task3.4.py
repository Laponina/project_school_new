# Добавьте возможность удаления ученика по заданному полному имени

import json

with open('Students_id.json', 'r+', encoding='UTF-8') as f:
    students = json.load(f)
pass

student = 'Красный Василий'



for el in students:
    if "%s %s" % (el["surname"], el["name"]) == student:
        el.clear()
        students.remove(el)



with open('Students_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(students, ensure_ascii=False)+'\n')
pass
