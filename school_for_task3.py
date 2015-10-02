import json

f = open('Students_prob.json', 'r+', encoding='UTF-8')
students = json.load(f)
f.close()
new_student = {
    "name": "Василий",
    "middle_name": "Петрович",
    "surname": "Красный",
    "school": "12 гимназия",
    "class": "7 А",
    "birth_day": "01.12.1996"
}
students.append(new_student)
f = open('Students_prob.json', 'w', encoding='UTF-8')
f.write(json.dumps(students, ensure_ascii=False) + '\n')

f.close()
