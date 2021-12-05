formatter = "{} {} {} {}"  # объявили строку форматтер со значение {}

print(formatter.format(1, 2, 3, 4))  # вывели на экран строку formatter с аргументами формат
print(formatter.format("раз", "два", "три", "четрые"))  # тоже самое объявили только с числами буквенными
print(formatter.format(True, False, False, True))  # вывели на экрна булеов значение true false
print(formatter.format(formatter, formatter, formatter, formatter))  #
print(formatter.format(
    "Спят в конюшне пони,",
    "начал пёс дремать,",
    "только мальчик Джонни",
    "не ложится спать!"
))
