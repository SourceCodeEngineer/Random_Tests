import random

while True:
    try:
        upper_range = int(input("This is a number guessing game, please select the upper range: "))
        break
    except:
        print("Only numbers are allowed!")
        continue

#Creating a random number
random_number = random.randrange(1, upper_range, 1)

print("You have 5 tries to guess the number.\n")

guesses = 0

while guesses < 5:

    guesses = guesses + 1
    while True:
        try:
            first_guess = int(input(("What is your guess?")))
            break
        except:
            print("Only numbers are allowed!")
            continue

    if first_guess == random_number:
        print(f"Congratulations, you guessed the right number. The number was {random_number}.")
        break

    elif first_guess < random_number:
        print("The number you guessed was lower than the number that was generated, try again!")
        #print(random_number)
        continue

    else:
        print("The number you guessed was higher than the number that was generated, try again!")
        #print(random_number)
        continue


print(f"This took you {guesses} guessses.")
