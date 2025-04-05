print("Welcome to random Password Generater!")
import random
import string

small_alphabet = string.ascii_lowercase
capital_alphabet = string.ascii_uppercase
num = string.digits
characters = "!@#$%^&*"

all_characters = small_alphabet + capital_alphabet + num + characters
length = int(input("Enter the length of password: "))
password = ''.join(random.sample(all_characters, length))

print("Password is: ", password)      
