burger = int (input())
side_order = int (input())
drink = int(input())
desert = int(input())

if burger == 1:
    a = 461
elif burger == 2:
    a = 431
elif burger == 3:
    a = 420
elif burger == 4:
    a = 0

if side_order == 1:
    b = 100
elif side_order == 2:
    b = 57
elif side_order == 3:
    b = 70
elif side_order == 4:
    b = 0

if drink == 1:
    c = 130
elif drink == 2:
    c = 160
elif drink == 3:
    c = 118
elif drink == 4:
    c = 0

if desert == 1:
    d = 167
elif desert == 2:
    d = 266
elif desert == 3:
    d = 75
elif desert == 4:
    d = 0

total_calories = (a + b + c + d)
print('Your total Calorie count is {}.'.format(total_calories))
