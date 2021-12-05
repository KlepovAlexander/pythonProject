def cheese_and_crackers(cheese_count, boxes_of_crackers):  # объвили функцию с именем cheese_and_crackers с аргументами
    print(f"У нас есть {cheese_count} сырков")  # вывели на экран значение функции chese_count
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")  # вывели на экран значение функции с помощью форматирования
    print("Этого достаточно для вечеринки!")
    print("Погнали!\n")  # вывели на экран слово и использовали символ новой строки(перенос)


print("Мы можем непосредственно передать числа функции:")
cheese_and_crackers(20, 30)  # передали число напрямую функции

print("ИЛИ, мы можем использовать переменные из нашего сценария:")
amount_of_cheese = 10  # создали переменную со значением 10 сырков
amount_of_crackers = 50  # создали переменную со значением 50 и назвали 50 пачек чипсов

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # использовали переменную со значением

print("Мы даже можем выполнять вычисления внутри функции:")
cheese_and_crackers(10 + 20, 5 + 6)  # выполнили значения прямо в фУНКЦИИ

print("И объединять переменные с вычисленями:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def apples_orange(orange_count):
    print(f"А также {orange_count} апельсинов")
    print("Этого хватит,чтобы наесться")
    print("Начнём пир!\n")


apple_one = input("сколько яблок?\n")
print(f"{apple_one} Яблок")
