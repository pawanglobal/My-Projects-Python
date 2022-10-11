N = int(input())

response = ''

for i in range(N):
    response = response + input()

answer_key = ''

for i in range(N):
    answer_key = answer_key + input()

correct = 0 

for i in range(N):
    if answer_key[i] == response[i]:
        correct = correct + 1

print(correct)
