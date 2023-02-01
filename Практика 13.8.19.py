num_tickets = int(input ('Введите количество билетов:'))
cost = 0
cost_pay = 0
for i in range(num_tickets):
    age = int(input('Введите возраст:'))
    if age < 18:
        cost += 0
        cost_pay +=1
        print('Билет бесплатный')
    elif 18 <= age < 25:
        cost += 990
        cost_pay += 1
        print('Стоимость билета 990 руб.')
    elif age >= 25:
        cost += 1390
        cost_pay += 1
        print('Стоимость билета 1390 руб.')

print(f'Общая стоимость билетов:{cost} руб.')

if num_tickets > 3 and cost > 4170 :
    cost = cost - ((cost/100)*10)
    print(f'Скидка 10% за {cost_pay}')
    print('Итоговая стоимость:', cost)

