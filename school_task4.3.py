# 3(HARD)➤ Напишите универсальную функцию, возвращающую все id учеников/учителей с заданными параметрами.
# Т.е. функция должна принимать список учителей/учеников и произвольный набор именованных параметров.
# Примеры:
# search([...], name=’Иван’, surname=’Иванов’) → вернет все id Ивановых Иванов
# search([...], class=’5 А’, surname=’Иванов’) → вернет всех учеников 5А класса ИЛИ всех учителей преподающих в 5А классе
# search([...], birth_day=’30.02.2000’) вернет всех учеников/учителей с указанной датой рождения
# Все возможные именованные аргументы соответствуют ключам словаря ученик/учитель

import json


def get_param(people,**kwargs ):
    result = []
    parametrs = []
    for key in kwargs:
        parametrs.append(key)
    for el in parametrs:
        if el == 'class_room':
            k = 'class'
        else:
            k = el
        for humane in people:
            if humane[k] == kwargs[el]:
                result.append(humane['id'])
    return result


with open('Teachers_id.json', 'r+') as f1:
    teachers = json.load(f1)
pass

with open('Students_id.json', 'r+') as f2:
    students = json.load(f2)
pass

# parametrs = ['name', 'surname']
# list_of_people = {'name': 'Иван', 'surname': 'Иванов'}
people = students

list_of_id = get_param(people,name='Кузин', class_room = '7 Г' )


list_of_id = list(set(list_of_id))

print(list_of_id)

#Сделать, чтобы можно было работать с классами учителей