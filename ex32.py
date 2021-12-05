the_count = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'апельсин', 'персик', 'абрикос']
change = [1, 'червонец', 2, 'полтинник', 3, 'сотня']
vegetables = ['помидор', 'морковь', 'свекла', 'огурец']

# цикл for первого типа обрабатывает список
for number in the_count:
    print(f"Счётчик {number}")

# то же,что и выше
for fruit in fruits:
    print(f"Фрукт:{fruit}")

for vegetable in vegetables:
    print(f"Овощ:{vegetable}")

# также можно обрабатывать смешанные списки
# обратите внимание,что использются символы {}, т.к неизвестен
# тип значения
for i in change:
    print(f"Я получил {i}")

# также мы можем создавать списки,начнём с пустого
elements = []
element = []
# затем используется функция range () для ограничения диапазона
for i in range(len(the_count)):
    print(f"Добавление {i} в список.")
    # append - функция для добавления элементов в список
    elements.append(i)

for i in range(10, 100):

    element.append(i)

# теперь мы их выводим
for i in elements:
    print(f"Номер элемента: {i}")

for i in element:
    print(f"номер овоща(зеля): {i}")
