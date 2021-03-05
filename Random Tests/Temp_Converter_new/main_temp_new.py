from def_file import cels_to_fahr
from def_file import fahr_to_cels
from def_file import user_decision

user_choice = user_decision()

if user_choice == 1:
    fahr, converted_temp = cels_to_fahr()
    print(f'{converted_temp}°C is {fahr}°F')
else:
    fahr, converted_temp = fahr_to_cels()
    print(f'{fahr}°C is {converted_temp}°F')
