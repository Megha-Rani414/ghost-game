# Ghost Game
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
ghost_door = 2
while feeling_brave:    
    print('Three doors ahead...')
    print('A ghost is behind one...')
    door_num = int(input('Out of these options\(1,2,3),Which door do you open?'))
    if door_num == 1:
        print('GHOST!')
        print('RUN AWAY!')
        score = score+1
        print('Game Over! You scored: ', score)
    elif door_num ==2:
        print("no ghost")
    elif door_num ==3:
        print("april fool")
        
    else:
        print('There was not a ghost.')
        print('You enter the next room...')
        
