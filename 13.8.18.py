bilets = int(input('Введите количество билетов '))
sum = 0
for i in range(bilets):
    age = int(input('Введите возраст посетителя '))
    if age < 18:
        print("Стоимость билета 0 руб")
    elif 18 <= age < 25:
        print(('Стоимость билета 990 руб'))
        sum = sum + 990
    elif 25 <= age:
        print(('Стоимость билета 1390 руб'))
        sum = sum + 1390
if bilets > 3:
    sum = sum * 0.9
    print('Сумма к оплате с учетом 10 % скидки: ', sum, 'руб')
else:
    print('Сумма к оплате: ', sum, 'руб')