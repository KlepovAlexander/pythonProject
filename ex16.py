from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename},если хотите его стереть,нажмите клавишу Enter.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C) ")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла....")
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у вас три строки.")

line1 = input("Строка 1:")
line2 = input("Строка 2:")
line3 = input("Строка 3:")

print("Это я запишу в файл.")

target.write(""" {line1} \n #{line2} \n {line3} \n""")
print("И наконец, я закрою файл.")
target.close()
