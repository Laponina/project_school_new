#Создайте функцию для добавления нового ученика в файл с данными
#Добавьте 5 новых учеников
import json

f = open('Students.json', 'r+', encoding='UTF-8')
students = json.load(f)
f.close()
new_student = {
    "name": "Георгий",
    "middle_name": "Борисович",
    "surname": "Рылеев",
    "school": "12 гимназия",
    "class": "7 А",
    "birth_day": "01.12.1996"
}
students.append(new_student)
f = open('Students.json', 'w', encoding='UTF-8')
f.write(json.dumps(students, ensure_ascii=False) + '\n')

f.close()
