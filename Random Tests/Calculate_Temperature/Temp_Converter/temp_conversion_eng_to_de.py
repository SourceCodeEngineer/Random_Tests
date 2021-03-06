# This program return temperatures from user input into the given choice
from function_for_calc import cels_to_fahr

def user_option():
    while True:
        try:
            print("Please select one of the following: \n \n 1: From Celsius to Fahrenheit \n 2: From Fahrenheit to Celsius \n")
            user_choice = input("What is your choice? ")
            user_choice = int(user_choice)
        except ValueError:
            print("Sorry, that was not a number! Please try again!")
            continue
        else:
            break
    return user_choice

print(cels_to_fahr())
