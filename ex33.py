import random

x = 1
while (x <= 10):
    A = random.randint(1, 10)
    x = x + 1
    if A%2==0:
        print(A, 'Чётное')
    else:
        print(A, 'нечётное')
