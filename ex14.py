from sys import argv

script, user_name, last_name = argv
prompt = "тут ответик >>>"

print(f"Привет {user_name},{last_name} я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {user_name} {last_name}?")
likes = input(prompt)

print(f"Есть ли у тебя домашние животные, если да,то какие?")
pets = input(prompt)

print("Как зовут твоё домашнее животное?")
pets_merk = input(prompt)

print(f"Где ты живёшь, {user_name} {last_name}?")
lives = input(prompt)

print("На каком ифончике ты работаешь?")
iphone_version = input(prompt)

print(f"""
Итак,ты ответила {likes} на вопрос, нравлюсь ли я тебе.
ты живёшь {lives}. Не представляю,где это.
у тебя {pets} по имени {pets_merk} 
И у тебя {iphone_version} ифунчик. Прекрасно
""")
