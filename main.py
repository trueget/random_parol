import random
c = int(input(' Какой длинны должен быть пароль? \n'))
s = ''
while c > 0:
    k = random.randint(48,122)
    if 97>k>90 or 64>k>57:
        continue
    else:
        s += chr(k)
        c -= 1
print(s)
