# Center 1 
def turn_around(): 
    for i in range(2): 
        turn_left()
        
def walk():
    while front_is_clear():
        put('token')
        move()
    if not front_is_clear(): 
        put('token')
        turn_around()
        x = (200 - carries_object('token'))//2
        for i in range(int(x)):
            move()
        done()
    
walk()

# Center 2 
think(10)
def turn_around(): 
    for i in range(2): 
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def walk(): 
    while not object_here() and front_is_clear(): 
        put('token')
        move()
        if wall_in_front():
            turn_left()
            if is_facing_north() and front_is_clear():
                put('token')
                move()
                turn_left()  
            elif front_is_clear(): 
                put('token')
                turn_left()
                turn_left()
                move()
                turn_right()
def trace_back(): 
    put('token') 
    turn_left()
    

walk()
            
