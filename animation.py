from termcolor import colored
import random
import time

# Randomly pick an element from the list
def pick(lst):
    return lst[random.randint(0, len(lst)-1)]

# List of colors supported by termcolor
colors = [
        "grey",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white"
]

# List of characters that are printed in art
chars = ['.', ',', '+', '*', '?', 'o', '&', '@']

# Uses pick to get random characters and random colors
# Speed increases exponentially
def generate_art():
    x = 1
    while(True):
        for i in range(100):
            for j in range(100):
                print(colored(pick(chars), pick(colors)), end='')
            print()
            time.sleep(x)
            x *= .95
generate_art()
