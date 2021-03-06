# Цель задания
# Научиться работать с циклом For и счетчиками.

#Что нужно сделать:
#Зайдите в файлы с заданиями и выполните так чтобы вывод соотвествовал условиям.

print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boy = int(input('Введите кол-во мальчиков: '))
girl = int(input('Введите кол-во девочек: '))
max = ''
min = ''
N = 0
row = ''

if girl > boy:
    max = 'G'
    min = 'B'
    N = boy
else:
    max = 'B'
    min = 'G'
    N = girl

if boy > girl * 2 or girl > boy * 2:
    print('Ответ: Нет решения')
else:
    for place in range(N):
        if boy == girl:
            row += min + max
            boy -= 1
            girl -= 1
        else:
            row += max + min + max
            if boy>girl:
              boy -= 2
              girl -= 1
            else:
              girl -= 2
              boy -= 1

    print(f'Ответ {row}')
