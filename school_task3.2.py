# По аналогии, добавьте возможность добавлять учителей
# Добавьте 2-3 новых учителя


import json

f = open('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()
new_teacher =   {
                "name": "Георгий",
                "middle_name": "Константинович",
                "surname": "Иванов",
                "school": "49 школа",
                "class": [
                "9 А",
                "10 Б",
                "11 В"
                ],
                "birth_day": "04.07.1988"
                }
teachers.append(new_teacher)
f = open('Teachers.json', 'w', encoding='UTF-8')
f.write(json.dumps(teachers, ensure_ascii=False)+'\n')

f.close()