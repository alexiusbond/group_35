from random import randint as generate_number, choice
import calculator
from person import Person
import sys
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 5))
print(calculator.multiplication(2, 5))

my_friend = Person('Jim', 20)
print(my_friend)
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
print('END')
