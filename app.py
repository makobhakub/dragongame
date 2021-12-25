import random as r
import time as t



def display_intro():
    print('You are in a land full of dragons and happen to be climbing a mountian in said land.')
    t.sleep(3)
    print('In front of yourself, you see 3 caves.')
    t.sleep(3)
    print('In one cave, the dragon is friendly and will not eat you')
    t.sleep(3)
    print('The other dragons are greedy and hungry, and will eat you on sight.')




def choose_cave():
    t.sleep(1.5)
    print('Which cave will you go into? (1, 2, or 3)')

    while True:

        cave = input()
        if cave == '1' or cave == '2' or cave == '3':
            break
        print('There are only 3 caves!, pick again')

    return cave



def check_cave(chosen_cave):
    print('you approach the cave, 2 steps at a time')
    t.sleep(3)
    print('2 steps more')
    t.sleep(3)
    print('final steps...')
    t.sleep(3)
    print('*You think to yourself* "do I really want to go into this cave" ')
    t.sleep(3)
    print('do you? (y or n)')
    final_choice = input()
    if final_choice == 'y':
        print('ץ๏ย คгє Շ๏๏ ๔єєק เภ Շђє ςคשє Շ๏ ﻮ๏ ๒คςк!')

    else:
        chosen_cave = choose_cave()


    friendly_cave = r.randint(1, 3)

    if chosen_cave == str(friendly_cave):
        print('...')
        t.sleep(2)
        print('you are not eaten by a dragon')
    else:
        print('...')
        t.sleep(2)
        print('you are eaten by a dragon')



choice_to_play_again = 'yEs'
while choice_to_play_again.upper() == 'YES' or choice_to_play_again.upper() == 'Y':
    display_intro()
    chosen_cave = choose_cave()
    check_cave(chosen_cave)
    print('Do you want to try again? (type "yes" or anything else if you want to end the game)')
    choice_to_play_again = input()

print('GOOD BYE! 👋')