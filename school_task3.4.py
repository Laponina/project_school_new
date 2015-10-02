# Добавьте возможность удаления ученика по заданному полному имени

import json

f = open('Students_prob.json', 'r+', encoding='UTF-8')
students = json.load(f)

f.close()

student = 'Красный Василий'

i=0
for el in students:
    if "%s %s" % (el["surname"], el["name"]) == student:
        list.remove (students[i])
    i = i+1


f = open('Students_prob.json', 'w', encoding='UTF-8')
f.write(json.dumps(students, ensure_ascii=False)+'\n')

f.close()
