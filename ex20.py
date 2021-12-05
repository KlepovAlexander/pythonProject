from sys import argv

script, input_file = argv


def print_all(f):  # создали функцию с название print all с аргументом f и прочитали её целиком
    print(f.read())


def rewind(f):  # создали функцию с названием rewind
    f.seek(0)  # установили позицию (seek) 0 параметром


def print_a_line(line_count, f):  # создали функцию с названием print a line, и прочитали построчно
    print(line_count, f.readline())


current_file = open(input_file)  # создали переменную с пользовательским файлом и открыли её с пользовательского ввода

print("Первым делом выведем файл целиком:\n")

print_all(current_file)  # вывели файл целиком

print("Теперь отомотаем назад, словно это кассета")

rewind((current_file))  # отмотка пользовательского файла

print("Выведем три строки:")

current_line = 1  # вывод первой строки
print_a_line(current_line, current_file)  #

current_line = 1
print_a_line(current_line, current_file)

current_line = 1
print_a_line(current_line, current_file)
