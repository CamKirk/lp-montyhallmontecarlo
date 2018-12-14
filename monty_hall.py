import random
import json

results = []
iterations = 20

win = 0
loss = 0

for guess in range(iterations):
    #setup the guess
    doors = ['a','b','c']
    contestant = random.choice(doors)
    prize = random.choice(doors)
    result = [contestant]

    #announcer removes a door randomly, can't be contestant or prize
    removal = contestant
    while(removal == contestant or removal == prize):
        removal = random.choice(doors)

    doors.remove(removal)
    

    #contestant switches to the 'other' door
    doors.remove(contestant)

    #both of these work!
    contestant = doors[0]
    #contestant = random.choice(doors)


    #output results
    result.append(contestant)
    results.append(result)

    #calc win/loss
    if contestant == prize:
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