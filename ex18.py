# сообщаем питону,что хотим создать (объявить) функцию, используя для этого команду def
#на строке ниже присвоили функции имя,мы её назвали print_two,но имя может быть любое,главное чтобы было понятно что она делает,короткое имя
def print_two(*args): #передаём какие-либо аргументы (*args),чтобы всё работало,нужно указать значение в круглых скобка, заканчивать строку надо символом двоеточия,а новую строку начать строку с отступа
  #после двоеточия все строки кода,имеющие отступ в четыре пробела,будут привязаны к функции (имени) print_two.
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_three_again(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("а я ничего не получаю")

print_two("Михаил", "Райтман")
print_three_again("Михаил", "Райтман", "аниме")
print_one("первый!")
print_none()