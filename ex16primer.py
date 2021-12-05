from sys import argv

script, cheburek = argv

text = open(cheburek)

print(f"Содержимое файла {cheburek}:")
print(text.read())

