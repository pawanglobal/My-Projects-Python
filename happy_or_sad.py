emotion = input()

happy = ':-)'
sad = ':-('

count = emotion.count(sad)
count_1 = emotion.count(happy)

if count == 0 and count_1 == 0:
    print('none')
elif count < count_1:
    print('happy')
elif count == count_1:
    print('unsure')
else:
    print('sad')