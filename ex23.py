import sys
script, encoding, error = sys.argv


def main (language_file, encoding, errors): #основная часть кода в функции main,она вызывается в конце сценария
    line = language_file.readline() # считывание одной строки

    if line: #имеет ли переменная line какое-либо значение.
        print_line(line, encoding, errors)
        return main (language_file,encoding,errors) # вызов функции возвращает в самое начало и снова запускает


def print_line(line, encoding, errors): # определение функции print_line которая отвечает за кодирование строки из файла languages.txt
    next_lang = line.strip() # удаление символов \n в конце строки line
    # название языка из languages с последующим преобразование в необработанные байты.
    #переменная next_lang представляет собой строку,для получения необр.байтов нужно вызвать функцию encode и закодировать строки
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors) # создание переменной cooked_string из raw_bytes ,

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8") # открытие файла languages.txt

main(languages, encoding, error) # вызов функции main с правильными параметрами,чтобы запустить работу цикла