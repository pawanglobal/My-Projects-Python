open_cases = int(input())

amounts = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000,
    1000000]

for i in range(open_cases):
    used = int(input())
    amounts[used] = 0

total = sum(amounts)

average = total / (10 - open_cases)

banker_offer = int(input())

if banker_offer > average:
    print('deal')
else:
    print('no deal')




