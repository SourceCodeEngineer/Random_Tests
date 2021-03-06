#Body Mass Index is a simple calculation using a person's height and weight.
# The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2
# is their height in metres squared. A BMI of 25.0 or more is overweight, while the
# healthy range is 18.5 to 24.9.
while True:

    while True:
        try:
            height = input("Please input your height in m: ")
            height = height.replace(",", ".")
            height = float(height)
        except ValueError:
            print("Sorry, that was not a number!")
            continue
        else:
            break

    while True:
        try:
            weight = int(input("Please input your weight in kg: "))
        except ValueError:
            print("Sorry, that was not a number!")
            continue
        else:
            break

    BMI = weight/(height**2)
    BMI = int(BMI)

    if BMI < 18.5:
        print(f'Your BMI is {BMI}, that means you are underweight!')
    elif BMI < 29.9:
        print(f'Your BMI is {BMI}, that means you are in healthy weight!')
    else:
        print(f'Your BMI is {BMI}, that means you are overweight!')

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
