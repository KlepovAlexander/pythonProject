print("""Ты пришёл домой и думаешь в какую комнату зайти
В какую дверь ты войдешь,в 1 или 2?""")

room = input("> ")

if room == "1":
    print("В своей комнате сидит кеша и играет в фар край")
    print("Твои действия?")
    print("1 - согнать кешу с компа")
    print("2 - дать ему поиграть в фар край")

    kesha = input("> ")

    if kesha == "1":
        print("Кеша обиделся и ушёл в армию.")
    elif kesha == "2":
        print("Кеша поиграл в фар край и проиграл,убежал домой заплакав")
    else:
        print(f"Это действие {kesha} было правильным.")
        print("Никитка радостный вернулся домой,ведь на следующий день ему на работу")

elif room == "2":
    print("Это комната родителей,там спит батя. Что будешь делать?")
    print("1. Скажу что кеша чмоня,на даёт поиграть в фк.")
    print("2. Посмотрю в зеркало и уйду.")

    pidorg = input("> ")

    if pidorg == "1":
        print("ты разбудил батю,батя дал тебе пизды,не надо будить батю.")
    elif pidorg == "2":
        print("батя спит,всё хорошо.")
