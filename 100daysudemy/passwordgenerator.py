import random

letters = ['a', 's', 'd', 'f']
digits = ['1', '2', '3', '4']
specials = ['\'', '"', '&', '*']
allowedchars = [letters, digits, specials]

length = int(input("Password length: "))
password = ""
for i in range(0, length + 1):
  password += allowedchars[random.randint(0, 2)][random.randint(0, 3)]

print(password)
