import random
import json

from monty_print import print_values

results_list = []
iterations = 5000

win = 0
loss = 0

for guess in range(iterations):
    #setup the guess
    doors = ['a','b','c']
    contestant_choice = random.choice(doors)
    prize_door = random.choice(doors)
    trial = [contestant_choice]

    #announcer removes a door randomly, can't be contestant_choice or prize_door
    to_remove = contestant_choice
    while(to_remove == contestant_choice or to_remove == prize_door):
        to_remove = random.choice(doors)

    doors.remove(to_remove)
    

    #contestant_choice switches to the 'other' door
    doors.remove(contestant_choice)

    #both of these work!
    contestant_choice = doors[0]
    #contestant_choice = random.choice(doors)


    #output results_list
    trial.append(contestant_choice)
    
    #calc win/loss
    if contestant_choice == prize_door:
        trial.append(True)
    else:
        trial.append(False)
        

    results_list.append(trial)

print_values(results_list)

