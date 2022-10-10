songs = 'ABCD'

button = 0

while button != 4:
    button = int(input())
    presses = int(input())
    for i in range(presses):
        if button == 2:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:1]
    output = ''
    for song in songs:
        output = output + song + ''
    print(output[:-1])