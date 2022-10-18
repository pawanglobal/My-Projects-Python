n = int(input())
yesterday_space = input()
today_space = input()

occupied = 0
for i in range(len(yesterday_space)):
    if yesterday_space[i] == 'C' and today_space[i] ==  'C':
        occupied = occupied + 1
print(occupied)