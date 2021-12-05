def add(a, b):
    print(f"Сложение {a} + {b}")
    return a + b

def percent (a, b):
    print(f"Процент {a} % {b}")
    return a % b

def subtract(a, b):
    print(f"Вычитание {a} - {b}")
    return a - b

def multiplay (a, b):
    print(f"Умножение {a} * {b}")
    return a * b

def divide (a, b):
    print(f"Деление {a} / {b}")
    return a / b


print("Давайте выполним несколько вычислений с помощью функций!")

age = add(30, 5)
percent_vision = percent(100.0, 45.0)
height = subtract(190, 4)
weight = multiplay(35, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Соотноешние зрения: {percent_vision}, Рост: {height}, Вес: {weight}, IQ: {iq}")

print("Это головоломка.")



what = add(age, subtract(height, multiplay(weight,divide(iq, 2))))

def divide_two (c, d):
    print(f"Деление {c} / {d}")
    return c / d

def multiplay_two (c, d):
    print(f"Умножение {c} * {d}")
    return c * d

def subtract_two (c, d):
    print(f"Вычитание {c} - {d}")
    return c - d

def add_two (c, d):
    print(f"Сложение {c} + {d}")
    return c + d

divide_two(iq, 2)
multiplay_two(weight, 62.5)
subtract_two(height, -4375.0)
add_two(age, -4189.0)
print("Получается: ", what, "Вы можете это вычислить вручную?")
print(f"{what}")