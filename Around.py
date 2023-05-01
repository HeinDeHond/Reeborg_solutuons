# Around 1
def walk():
    while front_is_clear(): 
        move()
        
def turn(): 
    while not front_is_clear():
        turn_left()

walk()
turn()
walk()
turn()
walk()
turn()
walk()

# Around 1 - variable 

def walk():
    while front_is_clear(): 
        move()
        
def turn(): 
    while not front_is_clear():
        turn_left()

def walk_x(x): 
    for i in range(x): 
        move()

walk()
turn()
walk()
turn()
walk()
turn()
walk()
turn()
walk_x(4)

# Around 1 - apple 
def walk():
    while front_is_clear(): 
        move()
        if object_here():
            take()
        elif at_goal():
            break
        while not front_is_clear():
            turn_left()
        
walk()

# Around 2 
def walk():
    while wall_on_right():
        move()
        if not front_is_clear():
            turn_left()
        if not wall_on_right(): 
            for i in range(3): 
                turn_left()
            move()
        if object_here():
            break

put()           
walk()

# Around 3 
# not proud of it 
think(10)
def turn_right():
    for i in range(3): 
        turn_left()
        
def walk():
    while wall_on_right() and front_is_clear():
        move()
        if object_here():
            break
        if not front_is_clear():
            turn_left()
        if not wall_on_right(): 
            turn_right()
            move()


put()  
turn_left()
move()
turn_right()
move()
move()
turn_right()
move()
turn_left()
walk()

walk()

# around 4 
think(10)
def turn_right():
    for i in range(3): 
        turn_left()
        
def walk():
    while wall_on_right() and front_is_clear():
        move()
        if object_here():
            break
        if not front_is_clear():
            turn_left()
        if not wall_on_right(): 
            turn_right()
            move()

def turn_around(): 
    for i in range(2): 
        turn_left()
               

put()  
turn_around()
move()
turn_right()
move()
walk()

