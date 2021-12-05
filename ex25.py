import random

for i in range(10):
    A = random.randint(1, 10)
    if A%2 == 0:
        print(A, 'Чётное')
    else:
        print(A, 'Нечётное')

