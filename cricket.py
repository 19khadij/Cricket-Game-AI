import random

def play():
    runs=[1,2,3,4,5,6]
    player=random.choice(runs)
    print(player)
    return player

#AI Algoritm 
#return value
value=0

player=play()

if value==player:
    print("Game Over")

else:
    print("Keep Playing!")
    play()
