#Создайте функцию для добавления нового ученика в файл с данными
#Добавьте 5 новых учеников
import json

with open('Students_id.json', 'r+', encoding='UTF-8') as f:
    students = json.load(f)
pass


id = students[len(students)-1]['id']

new_student = {
    "id":id+1,
    "name": "Георгий",
    "middle_name": "Борисович",
    "surname": "Рылеев",
    "school": "12 гимназия",
    "class": "7 А",
    "birth_day": "01.12.1996"
}
students.append(new_student)
with open('Students_id.json', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(students, ensure_ascii=False) + '\n')

pass
