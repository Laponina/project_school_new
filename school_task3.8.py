# Добавьте возможность удалять указанные классы у указанного преподавателя
import json

def get_name (data, teacher_class, teacher_name):
    for teacher in data[get_name(teachers, teacher_name)]:
        if teacher_class == '%s %s %s' % (teacher['surname'], teacher['name'], teacher['middle_name']):
            return data.index(teacher)

def get_name (data, teacher_name):
    for teacher in data:
        if teacher_name == '%s %s %s' % (teacher['surname'], teacher['name'], teacher['middle_name']):
            return data.index(teacher)


f = open('Teachers.json', 'r+', encoding='UTF-8')
teachers = json.load(f)
f.close()

form = "9 А"
name = 'Иванов Георгий Константинович'



teachers[get_name(teachers, name)]['class'].remove(teachers[get_name(teachers, name)]['class'][get_index(teachers, form)])