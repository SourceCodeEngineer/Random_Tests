#This is a number generator for a terminal

from func_for_number_generator import upperlimit
import random

upper_limit = upperlimit()

random_number = random.randrange(0, upper_limit, 1)

print(f"Your random number is {random_number}.")
