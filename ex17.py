from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копирование {from_file}.")
input("Начать копирование??")

print(f"Копирование из файла {from_file} в файл {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Исходный файл имеет размер {len(to_file)} байт")

print(f"Файл существует? {exists(to_file)}")
print("Готов, нажмите клавишу Enter для продолжения или CTRL+C для отмены.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Отлично, все сделано.")

out_file.close()
