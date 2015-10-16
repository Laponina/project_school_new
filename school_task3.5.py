# Добавьте возможность удаления всех учеников из указанного класса
import json

form = '7 А'
with open('Students_id.json', 'r+', encoding='UTF-8') as f:
    students = json.load(f)
pass

for el in students:
    if el['class'] == form:
        el.clear()
        students.remove(el)

with open('Students_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(students, ensure_ascii=False))
pass
