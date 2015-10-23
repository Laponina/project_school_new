# Аналогично сделайте удаление учителя по полному имени(Ф.И.О.)
import json

with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass

teacher = 'Иванов Георгий Константинович'

for el in teachers:
    if "%s %s %s" % (el["surname"], el["name"], el["middle_name"]) == teacher:
        el.clear()
        teachers.remove(el)

with open('Teachers_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
pass
