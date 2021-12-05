# Ассоциации аббревитур с названиями стран СНГ
CIS_countries = {
    'Россия': 'RU',
    'Украина': 'UA',
    'Белоруссия': 'BLR',
}
# Набор стран и городов (столиц)
cities = {
    'RU': 'Москва',
    'UA': 'Киев',
    'BLR': 'Минск'
}

# Вывод городов
print('-' * 10)
print("В стране RU есть город: ", cities['RU'])
print("В стране UA есть город: ", cities['UA'])
print("В стране BLR есть город: ", cities['BLR'])

# Вывод стран
print('-' * 10)
print("Аббревиатура России:", CIS_countries['Россия'])
print("Аббревиатура Украины:", CIS_countries['Украина'])
print("Аббревиатура Белорусси", CIS_countries['Белоруссия'])

# с учётом страны и словаря городов
print('-' * 10)
print("Столицей в России является:", cities[CIS_countries['Россия']])
print("Столицей в Украине является:", cities[CIS_countries['Украина']])
print("Столицей в Белоруссии является:", cities[CIS_countries['Белоруссия']])

# вывод аббревиатур всех стран
print('-' * 10)
for CIS_countries_state, abbrev in list(CIS_countries.items()):
    print(f"{CIS_countries_state} имеет аббревиатуру {abbrev}")

# вывод всех городов в странах
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"В стране {abbrev} есть город {city}")

# Сразу оба типа данных
print('-' * 10)
for CIS_countries_state, abbrev in list(CIS_countries.items()):
    print(f"В стране {CIS_countries_state} используется аббревиатура {abbrev}")
    print(f"И есть город {cities[abbrev]}")

