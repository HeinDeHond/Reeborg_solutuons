# Storm 0
def turn_right(): 
    for i in range(3): 
        turn_left()

def turn_around(): 
    turn_left()
    turn_left()


def pickup(): 
    while not at_goal() and front_is_clear(): 
        while object_here(): 
            take()
        if not object_here():
            move()
    if not front_is_clear(): 
        while object_here(): 
            take()

def walk(): 
    turn_around()
    for i in range(5): 
        move()


            
move()
pickup()
walk()
turn_right()
while carries_object():
    toss()
done()

# Storm 2 
def turn_right(): 
    for i in range(3): 
        turn_left()

def turn_around(): 
    turn_left()
    turn_left()

def walk(): 
    for i in range(5): 
        move()
    turn_left()

move_count = 0
def pickup(): 
    global move_count
    while not at_goal() and front_is_clear() and move_count < 32:
        while object_here(): 
            take()
        if not object_here():
            move()
            move_count+=1 
        if not front_is_clear() and is_facing_north(): 
            while object_here(): 
                take()
            turn_left()
            move()
            turn_left()
            move_count+=1 
        if not front_is_clear() and not is_facing_north(): 
            while object_here(): 
                take()
            turn_right()
            move()
            turn_right()
            move_count+=1
            
def return_home():
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    done()


walk()
pickup()
move()
while object_here():
    take()
while carries_object():
    toss()
return_home()







