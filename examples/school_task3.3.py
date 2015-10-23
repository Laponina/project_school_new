# Добавьте возможность добавлять классы (которые он ведет) к указанному преподавателю

import json

with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass

teacher = 'Владимир Сергеевич'
form = '11 Г'


for el in teachers:
    if "%s %s" % (el["name"], el["middle_name"]) == teacher:
        el["class"].append(form)

with open('Teachers_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
pass
