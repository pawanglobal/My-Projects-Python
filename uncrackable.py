password = input()

gud_char = 0
upper_chars = 0
lower_chars = 0
digit_chars = 0

for char in password:
    if char.islower() or char.isupper() or char.isdigit():
        gud_char = gud_char + 1
    if char.isupper():
        upper_chars = upper_chars + 1
    elif char.islower():
        lower_chars = lower_chars + 1
    elif char.isdigit():
        digit_chars = digit_chars + 1
if (len(password) >= 8 and len(password) <=12
        and gud_char == len(password)
        and lower_chars >=3 and upper_chars >= 2 and digit_chars >= 1):
    print('Valid')
else:
    print('Invalid')
