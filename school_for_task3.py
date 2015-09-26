
import json

f = open('Students_prob.json', 'r+', encoding='UTF-8')
students = json.load(f)
new_student = {
            "name": "Василий",
            "middle_name": "Петрович",
            "surname": "Красный",
            "school": "12 гимназия",
            "class": "7 А",
            "birth_day": "01.12.1996"
            }
students.append(new_student)
for el in students:
    f.write(json.dumps(el['name'], ensure_ascii=False))


f.close()