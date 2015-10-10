# Добавьте возможность удалять указанные классы у указанного преподавателя
import json

def get_index (data, teacher_class, teacher_name):
    for el in data[teacher_name]['class']:
        if el == teacher_class:
            return data.index(teacher_class)

def get_name (data, teacher_name):
    for teacher in data:
        if teacher_name == '%s %s %s' % (teacher['surname'], teacher['name'], teacher['middle_name']):
            return data.index(teacher)


f = open('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

form = "9 А"
name = 'Иванов Георгий Константинович'

f = open('Teachers.json', 'w', encoding='UTF-8')

teachers[get_name(teachers, name)]['class'].remove(teachers[get_name(teachers, name)]['class'][get_index(teachers, form, get_name(teachers, name))])
f.write(json.dumps(teachers, ensure_ascii=False) + '\n')
f.close