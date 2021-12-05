print("Давайте попрактикуемся!")
print('Вы должны знать об управляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами.')

poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\tи никогда не отпускать!
"""

print("_______________________________")
print(poem)
print("_______________________________")


five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятёрка {five}")

def sectret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = sectret_formula(start_point)

#это ещё один способ форматирования строки
print("Начиная с: {}".format(start_point))
#Так же,как со строкой f""
print(f"Унас есть {beans} бобов, {jars} банок и {crates} ящиков.")

start_point = start_point / 10

print("Мы также можем сделать это таким образом:")
formula = sectret_formula(start_point)
#простой способ применить список к форматируемой строке
print("У нас есть {} бобов, {} банок и {} ящиков.".format(*formula))
