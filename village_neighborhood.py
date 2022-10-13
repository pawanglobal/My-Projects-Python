n = int(input())

lst = []

for number in range(n):
    number = int(input())
    lst.append(number)
    lst.sort()


left = (lst[1] - lst[0])/2
right = (lst[2] - lst[1])/2
min_size = left + right

for i in range (2, n-1):
    left = (lst[i] - lst[i - 1])/2
    right = (lst[i + 1] - lst[i])/2
    size = left + right
    if size < min_size:
        min_size = size
print(min_size)