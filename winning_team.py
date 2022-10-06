three_pt_apple = int(input ())
two_pt_apple = int(input())
one_pt_apple = int(input())

three_pt_bana = int(input())
two_pt_bana = int(input())
one_pt_bana= int(input())

apple_total = three_pt_apple*3 + two_pt_apple*2 + one_pt_apple*1
banana_total= three_pt_bana*3 + two_pt_bana*2 + one_pt_bana*1

if (apple_total) > (banana_total):
    print('A')
elif (apple_total) < (banana_total):
    print('B')
else:
    print('T')