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
