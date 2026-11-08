def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    elif front_is_clear():
        move()