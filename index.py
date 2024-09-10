import random


fname = input("enter your fname")
random_numbers = [random.randint(4,9) for _ in range(10)]
output = print(*random_numbers)

username = fname + "@" + output