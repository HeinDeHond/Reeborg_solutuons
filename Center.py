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
