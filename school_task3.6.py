# Аналогично сделайте удаление учителя по полному имени(Ф.И.О.)
import json

f = open('Teachers_id.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

teacher = 'Иванов Георгий Константинович'

for el in teachers:
    if "%s %s %s" % (el["surname"], el["name"], el["middle_name"]) == teacher:
        el.clear()
        teachers.remove(el)

f = open('Teachers_id.json', 'w', encoding='UTF-8')
f.write(json.dumps(teachers, ensure_ascii=False) + '\n')

f.close()
