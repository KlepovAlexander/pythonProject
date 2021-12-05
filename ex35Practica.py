def one_car():
    print("Здесь стоит Chevrolet lacetti")
    print("Чёрного цвета 21 века")


def two_car():
    print("Здесь стоит Kia rio x-line")
    print("Серого цвета 20 года")
    print("Сесть в машину kia или выбрать другой гараж?")

    choise_car_user = input("> ")

    if "Сесть в машину kia" in choise_car_user:
        car_movement()
    elif "Выбрать другой гараж" in choise_car_user:
        one_car()
    else:
        print("Ты не выбрал ни одно из перечисленных")


def start_avto():
    print("Ты стоишь около двух закрытых гаражей")
    print("Там находятся два неизвестных автомобиля")
    print("Какой гараж ты откроешь?")

    choise_avto = input("> ")

    if choise_avto == "первый":
        one_car()
    elif choise_avto == "второй":
        two_car()
    else:
        print("Ты ничего не выбрал,попробуй запусти игру ещё раз!")


def car_movement():
    zavesti_avto = input(" >")

    if zavesti_avto == ("Завести"):
        print("Машина заведена")
    elif zavesti_avto != ("Завести"):
        print("Вернись и заведи машину")
    else:
        print("Ты ничего не сделал,запусти игру ещё раз")


start_avto()
car_movement()
