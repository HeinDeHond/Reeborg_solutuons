# Hurdle 1 & 2 & 3 & 4 
def turn_right():
    for i in range(3): 
        turn_left()
        
def turn_around(): 
    for i in range(2): 
        turn_left()

def walk(): 
    turn_left()
    count_wall = 0 
    while wall_on_right(): 
        count_wall += 1
        move()
    turn_right()
    move()
    turn_right()
    while count_wall > 0: 
        move()
        count_wall -= 1 
    turn_left()

while not at_goal(): 
    if wall_in_front(): 
        walk()
    else: 
        move()


