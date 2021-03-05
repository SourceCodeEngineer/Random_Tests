from temp_conversion_eng_to_de import user_option

def cels_to_fahr():

    user_choice = user_option()

    if user_choice == 1:
        while True:
            try:
                temp_cels = input(
                    print("You selected Celsius to Fahrenheit. Please give us the temperature in Celsius: "))
                temp_cels = int(temp_cels)
                converted_temp = (temp_cels * 9 / 5) + 32
            except ValueError:
                print("Sorry, that was not a number! Please try again!")
                continue
            else:
                break

        return temp_cels + " °C is " + converted_temp + " °F."

    else:
        while True:
            try:
                temp_fahr = input(print("You selected Fahrenheit to Celsius. Please give us the temperature in Fahrenheit: "))
                temp_fahr = int(temp_fahr)
                converted_temp = (temp_fahr - 32) * 5/9
            except ValueError:
                print("Sorry, that was not a number! Please try again!")
                continue
            else:
                break

        print(f'{temp_fahr}°F is {converted_temp}°C \n')
