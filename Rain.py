# Rain o
def turn_right():
    for i in range(3): 
        turn_left()
        
def trace_wall(): 
    while wall_on_right() and front_is_clear(): 
        move()
        if wall_on_right() and not front_is_clear(): 
            turn_left()
    if not wall_on_right(): 
        turn_right()
        build_wall()
        turn_left()
        pass

def trace_wall_opening(): 
    while wall_on_right() and front_is_clear(): 
        move()
        if wall_on_right() and not front_is_clear(): 
            turn_left()
    if not wall_on_right(): 
        done()

move()
turn_right()
move()
trace_wall()
trace_wall_opening()

# Rain 1
think(100) 
def turn_right():
    for i in range(3): 
        turn_left()
        
def trace_wall(): 
    while wall_on_right() and front_is_clear(): 
        move()
        if wall_on_right() and not front_is_clear(): 
            turn_left()
    if not wall_on_right(): 
        turn_right()
        build_wall()
        turn_left()
        pass

move()
turn_right()
move()
while not at_goal(): 
    trace_wall()
while at_goal():
    done()

# Rain 2 
think(200) 
def turn_right():
    for i in range(3): 
        turn_left()

def turn_around():
    for i in range(2): 
        turn_left()
        
def trace_wall(): 
    while wall_on_right() and front_is_clear(): 
        move()
    if wall_on_right() and not front_is_clear(): 
        turn_left()
    num_walls = 0
    if not wall_on_right(): 
        move() 
        if wall_on_right():
            turn_around()
            move()
            turn_left()
            build_wall()
            turn_left()
        elif not wall_on_right(): 
            turn_around()
            move()
            turn_left()
            move()

move()
move()
move()
turn_right()
move()
while at_goal():
    done()
while not at_goal(): 
    trace_wall()

