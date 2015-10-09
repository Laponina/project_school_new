# Добавьте возможность добавлять классы (которые он ведет) к указанному преподавателю

import json

f = open('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

teacher = 'Владимир Сергеевич'
form = '10 Г'

for el in teachers:
    if "%s %s" % (el["name"], el["middle_name"]) == teacher:
        el["class"].append(form)
f = open('Teachers.json', 'w', encoding='UTF-8')
f.write(json.dumps(teachers, ensure_ascii=False) + '\n')

f.close()
