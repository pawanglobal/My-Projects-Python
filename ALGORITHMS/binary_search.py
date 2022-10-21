def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low < high:
        mid = len(lst) // 2
        guess = lst[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid
        if guess > item:
            high = mid

my_list = [1, 2, 3, 4, 5]

a = binary_search(my_list, 3)
print(my_list[a])



    