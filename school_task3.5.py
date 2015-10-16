# Добавьте возможность удаления всех учеников из указанного класса
import json

form = '7 А'
f = open('Students_id.json', 'r+', encoding='UTF-8')
students = json.load(f)
f.close

for el in students:
    if el['class'] == form:
        el.clear()
        students.remove(el)

f = open('Students_id.json', 'w', encoding='UTF-8')
f.write(json.dumps(students, ensure_ascii=False))
f.close()
