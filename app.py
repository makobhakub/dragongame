import random
import time

def display_intro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')


def choose_cave():
    while True:
        print('Which cave will you go into? (1 or 2)')
        cave = input()
        if cave == '1' or cave == '2':
            break
        print('that is not a valid decision, choose either 1 or 2')



choose_cave()
