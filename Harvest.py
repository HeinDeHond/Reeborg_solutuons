# Harvest 1 
think(10)
def turn_right():
    for i in range(3): 
        turn_left()
def turn_around(): 
    for i in range(2): 
        turn_left()

def walk(): 
    while front_is_clear(): 
        move()
        if object_here(): 
            take()
            if carries_object('carrot') == 36: 
                done()
        if wall_in_front(): 
            turn_left()
            if is_facing_north(): 
                move()
                turn_left()
            else: 
                turn_around()
                move()
                turn_right()

walk()

# Harevst 2 
think(10)
def turn_right():
    for i in range(3): 
        turn_left()
def turn_around(): 
    for i in range(2): 
        turn_left()

def walk(): 
    while front_is_clear(): 
        move()
        while object_here(): 
            take()
        if wall_in_front(): 
            turn_left()
            if is_facing_north(): 
                move()
                turn_left()
            else: 
                turn_around()
                if wall_in_front(): 
                    done()
                move()
                turn_right()

walk()
               
# Harvest 3 
think(100)
def turn_right():
    for i in range(3): 
        turn_left()
def turn_around(): 
    for i in range(2): 
        turn_left()

def walk(): 
    for i in range(9): 
        move()
    turn_left()
    move()
    turn_left()
    for i in range(9): 
        move()
    turn_right()
    move()
    turn_right()
        
    
def harvest_row(): 
    move()
    move()
    for i in range(6): 
        if object_here('carrot'): 
            take('carrot')
            if object_here('carrot'): 
                take('carrot')
                if object_here('carrot'): 
                    take('carrot') 
        if not object_here('carrot'):
            put('carrot')
            move()
    move()
    turn_left()
    if is_facing_north(): 
        move()
        turn_left()
    else:
        turn_around()
        move()
        turn_right()
   
    
    
walk()
harvest_row()
harvest_row()
harvest_row()
harvest_row()
harvest_row()
harvest_row()
done()
