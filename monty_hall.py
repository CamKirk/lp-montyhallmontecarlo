import random
import json

results = []
iterations = 20

win = 0
loss = 0

for guess in range(iterations):
    #setup the guess
    doors = ['a','b','c']
    contestant_choice = random.choice(doors)
    prize_door = random.choice(doors)
    result = [contestant_choice]

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


    #output results
    result.append(contestant_choice)
    results.append(result)

    #calc win/loss
    if contestant_choice == prize_door:
        win+=1
    else:
        loss+=1

prior = {
    "a": 0,
    "b": 0,
    "c": 0
}

posterior = {
    "a": {
        "a": 0,
        "b": 0,
        "c": 0
    },
    "b": {
        "a": 0,
        "b": 0,
        "c": 0
    },
    "c": {
        "a": 0,
        "b": 0,
        "c": 0
    }
}
for i,j in results:
    prior[i]+=1
    posterior[i][j]+=1

print(json.dumps(prior, indent=1))
print(json.dumps(posterior, indent=1))
print((win, loss, win/(win+loss)))