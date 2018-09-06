import random

min = 1
max = 45
numbers_per_line = 6

number_of_quick_picks = int(input("How many quick picks? "))

for pick in range(number_of_quick_picks):
    quick_pick = []
    for list in range(numbers_per_line):
        number = random.randint(min, max)
        while number in quick_pick:
            number = random.randint(min, max)
        quick_pick.append(number)
    quick_pick.sort()

    print(" ".join("{:2}".format(number) for number in quick_pick))

