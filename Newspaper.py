# Newspaper 0
def turn_right():
    for i in range(3): 
        turn_left()
        
def turn_around(): 
    for i in range(2): 
        turn_left()

def move_left(): 
    move()
    move()

def three_steps(): 
    move()
    turn_right()
    move_left()
    turn_left()

def three_steps_down(): 
    move()
    move()
    turn_left()
    move()
    turn_right()

def move_up():
    for i in range(3): 
        three_steps()

def move_down(): 
    for i in range(3): 
        three_steps_down()
        
take()
turn_left()
move_up()
put()
turn_left()
move_down()

# Newspaper 1
def turn_right():
    for i in range(3): 
        turn_left()
        
def turn_around(): 
    for i in range(2): 
        turn_left()

def move_left(): 
    move()
    move()

def three_steps(): 
    move()
    turn_right()
    move_left()
    turn_left()

def three_steps_down(): 
    move()
    move()
    turn_left()
    move()
    turn_right()

def move_up():
    for i in range(3): 
        three_steps()

def move_down(): 
    for i in range(3): 
        three_steps_down()
        
take()
turn_left()
move_up()
put()
while object_here('token'): 
    take('token')
turn_left()
move_down()
