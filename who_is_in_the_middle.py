weight_1 = int(input())
weight_2 = int(input())
weight_3 = int(input())

if weight_1> weight_2 > weight_3 or weight_3 > weight_2 > weight_1:
    print(weight_2)
elif weight_2 > weight_1 > weight_3 or weight_3 > weight_1 > weight_2:
    print(weight_1)
else:
    print(weight_3)