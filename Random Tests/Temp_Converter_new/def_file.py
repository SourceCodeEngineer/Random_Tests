def user_decision():
    while True:
        try:
            user_choice = input("Please select one of the following:  \n 1: From Celsius to Fahrenheit  \n 2: From Fahrenheit to Celsius\n\nYour selection:  ")
            user_choice = int(user_choice)
        except ValueError:
            print("Sorry, that was not a number! Please try again!")
            continue
        else:
            break
    return user_choice


def cels_to_fahr():
    while True:
        try:
            temp_cels = input("Please enter the Celsius here: ")
            temp_cels = int(temp_cels)
            converted_temp = (temp_cels * 9 / 5) + 32
        except:
            return "Not a number, try again!"
        else:
            break
    return converted_temp, temp_cels

def fahr_to_cels():
    while True:
        try:
            temp_fahr = input("You selected Fahrenheit to Celsius. Please give us the temperature in Fahrenheit: ")
            temp_fahr = int(temp_fahr)
            converted_temp = (temp_fahr - 32) * 5 / 9
        except ValueError:
            return "Sorry, that was not a number! Please try again!"
            continue
        else:
            break
    return temp_fahr, converted_temp
