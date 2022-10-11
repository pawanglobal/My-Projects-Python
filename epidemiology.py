P = int(input())
N = int(input())
R = int(input())

prev_day = N
day = 0


while N <= P:
    N = N + prev_day * R
    prev_day = prev_day * R
    day = day + 1

print(day) 
