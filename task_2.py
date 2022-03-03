print('Задача 2. Долги')

# МирПрогБанк наконец-то разделил законопослушных граждан и должников и поместил их в разные базы.
# Но банк не торопится как-то слишком сильно давить на возврат денег.
# Сейчас операторам банка дали задание
# позвонить каждому пятому должнику из списка (они нумеруются с нуля) и спросить,
# сколько примерно денег каждый из них задолжал банку.
#
# Напишите программу,
# которая принимает на вход количество должников,
# затем спрашивает у каждого пятого (начиная с 0) его долг.
# В конце выводится общая сумма долгов.

# Пример:
#
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

total_debtor = int(input('Количество должников? '))
total_duty = 0

for debtor in range(1, total_debtor, 5):
    print(f"Должник с номером {debtor - 1}")
    total_duty += int(input('Сколько должны? '))
print(f"Общая сумма долга: {total_duty}")