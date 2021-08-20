import random

# Matthias Gilbert
# gets the number of sides your dice has


def get_dice_side():
    sides = input("How many sides does your dice have? Type 'exit' if you want to quit: ")
    if sides.casefold() == 'exit':
        print('Goodbye have a lovely day')
        exit()
    try:
        return int(sides)
    except ValueError:
        print('Invalid response please enter numbers')


# gets the amount of dice being rolled


def dice_amount():
    amount = input("How many dice would you like to roll? Type 'exit' if you want to quit: ")
    if amount.casefold() == 'exit':
        print('Goodbye have a lovely day')
        exit()
    try:
        return int(amount)
    except ValueError:
        print('Invalid response please enter numbers')


# combines the other two and uses them to roll what the user wants


def dice_roll(side, number):
    total = []
    for n in range(number):
        roll = random.randint(1, side)
        total.append(roll)
    if number == 1:
        print('Your roll was: ', total)
    else:
        print('Your rolls total was: ', sum(total))
