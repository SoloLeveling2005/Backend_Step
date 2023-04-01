# todo Домашнее задание №12. Строки

# todo Задание №1.
user_input = 'Hello world'
output = " ".join([i for i in user_input.split(' ')])
print('Задание №1:')
print(output)

# todo Задание №2.
user_input = 'Hello world'
mass = user_input.split(' ')
output = mass.count(mass[-1]) + 1
print('\n\nЗадание №2:')
print(output)

# todo Задание №3.
user_input = 'В 2020 году я буду все делать вовремя!'
output = user_input.replace('2020', '2021')
print('\n\nЗадание №3:')
print(output)

# todo Домашнее задание №13. Списки
user_input = [1, -3, 5, -6, -10, 13, 4, -8]
summ = 0
sum_2 = 1
for i in user_input:
    if summ != 0 or sum_2 == 1:
        summ += i
        sum_2 += i**2
    else:
        break
sum_2 -= 1
print('\n\nЗадание №3:')
print("SUM * 2 = ",sum_2)
