think(50)
def turn_right():
    for i in range(3): 
        turn_left()
        
def turn_around(): 
    for i in range(2): 
        turn_left()

def solve(): 
    if right_is_clear(): 
        turn_right()
        move()
    elif front_is_clear(): 
        move() 
    else: turn_left()
           
        

while not at_goal(): 
    solve()
else: 
        done()


