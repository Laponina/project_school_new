# По аналогии, добавьте возможность добавлять учителей
# Добавьте 2-3 новых учителя


import json

with open('Teachers_id.json', 'r+', encoding='UTF-8') as f:
    teachers = json.load(f)
pass


id = teachers[len(teachers)-1]['id']

new_teacher =   {
                'id': id+1,
                "name": "Григорий",
                "middle_name": "Борисович",
                "surname": "Терентьев",
                "school": "10 гимназия",
                "class": [
                "9 А",
                "9 Б",
                "9 Д"
                ],
                "birth_day": "04.07.1988"
                }
teachers.append(new_teacher)
with  open('Teachers_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(teachers, ensure_ascii=False)+'\n')
pass