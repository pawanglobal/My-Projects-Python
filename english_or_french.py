N = int(input())

find_t = 0
find_s = 0

for i in range(N):
    words = input()
    for char in words:
        if char == 't' or char == 'T':
            find_t = find_t + 1
        if char == 's' or char == 'S':
            find_s = find_s + 1
if find_t > find_s:
    print('English')
else:
    print('French')