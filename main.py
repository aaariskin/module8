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