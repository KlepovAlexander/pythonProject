from sys import argv # передали аргументы сценарию python  и добавили в сценарии новые функции из доступных python agrv переменная содержит аргументы которые нужно передать

sript, filename = argv # распаковали переменную argv,чтобы вместо хранения всех аргументов назначить 2 переменные,с которыми можно работать. или взяли всё содержимое и argv и распаковали его с назначением в качестве значений переменных

txt = open(filename) # открывает iilename

print(f"Содержимое файла {filename} :") # вывод текста в переменной filename
print(txt.read()) # чтение содержимого

print("Снова введите имя файла :")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
