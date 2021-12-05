people = 20
cats = 30
dogs = 15


if people < cats:
    print("Слишком много кошек! Мир обречён!")

if people > cats:
    print("Не так много кошек,мир спасён!")

if people < dogs:
    print("Мир утоп в слюнах!")

if people > dogs:
    print("Не всё так плохо!")


dogs += 5

if people >= dogs:
    print("Людей больше или столько же сколько, сколько собак.")

if people <= dogs:
    print("Людей меньше или столько же, сколько собак.")



if people == dogs:
    print("Людей столько же,сколько и собак")