print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы: '))

total_expenses = 0
percent = 0
summ = 0

for month in range(1, 11):
    if month != 1:
        percent = 0.03
    total_expenses += expenses + expenses * percent

summ = total_expenses - educational_grant * 10
if educational_grant * 10 > total_expenses:
    print(f'По итогу уч. года студент в плюсе на {summ*(-1)}')
else:
    print(f'Студенту необходимо попросить у родителей {summ}')