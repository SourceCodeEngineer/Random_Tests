import string
import random

while True:
    try:
        length = int(input("Please select the length of your random generated password: "))
    except:
        print("Not a number! Please try again!")
    else:
        break

password_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(password_characters) for element in range(length))

print("Random password is:", password)
