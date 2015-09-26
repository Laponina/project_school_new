#Создайте функцию для добавления нового ученика в файл с данными
#Добавьте 5 новых учеников
import json
def append_students(f):
    students = json.load(f)
    new_student = {
                "name": "Василий",
                "middle_name": "Петрович",
                "surname": "Красный",
                "school": "12 гимназия",
                "class": "7 А",
                "birth_day": "01.12.1996"
                }
    students = new_student + students
    json.dumps(students, ensure_ascii=False)
    return students

f = open('Students_prob.json', 'w', encoding='UTF-8')

new_students = append_students(f)
print(new_students)
f.close()

