types_of_people = 10  # объявление переменной с типами людей
x = f"Существует {types_of_people} типов людей."  # использование переменной с типами людей

binary = "python"  # инициализация переменной
do_not = "нет"  # тоже самое что выше
y = f"Те кто понимает {binary}, и те, кто - {do_not}."  #использование переменной после инициализации

print(x)  # вывод переменной х
print(y)  # вывод переменной у

print(f"Я сказал: {x}")  # вывод переменной и форматирование со сторокой х
print(f"А ещё я сказал: ' {y}' ")  # вывод переменной и форматирование со строкой у

hilarious = False  # объявления булева значения фолс
joke_evaluation = "Разве это не смешно?! {}"  # создание переменной для булева значения

print(joke_evaluation.format(hilarious))  # вывод на экран с форматированием уже созданной строки hilarious

w = "Это часть строки слева..."  #объявление новой переменной
e = "а это справа."  # объявление новой перменной

print(w + e)  # вывод на экран двух переменных
