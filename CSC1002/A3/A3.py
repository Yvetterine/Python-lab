import turtle
import random
import time

g_snake = [[0,0]]   # The initial snake list
g_direction = 1      # Indicate direction
g_count = 5           # Add how many tail
g_dic_position = {}     # Record the position of each of foods
remain_or_not = True    # Go to the loop
create_number = True    # Go to the loop
g_eat_how_many = 0      # Record eat how many food
g_eat_which = []             # Record eat which foods
g_list_hide = []                # Record the hide numbers
g_list_appear = [1, 2, 3, 4, 5]          # Record the numbers which can appear
g_list_appear_real = [1, 2, 3, 4, 5]   # Distinguish between being eaten and being hidden
not_end = True     # Go to the loop
g_screen = None    # A blank variable for later
g_border = None    # A blank variable for later
g_indication = None     # A blank variable for later
g_introduction = None     # A blank variable for later
monster_x = 99999    # Record the x-coordinates of the monster
monster_y = 99999    # Record the y-coordinates of the monster
monster_item = None     # Record the snake in turtle
g_monster = None       # A blank variable for later
add_or_not = True     # Determine whether to extend the tail
hide = True        # Determine whether the number is hidden or displayed
dic_number_items = {}    # Record foods in turtle
g_hide = []          # Record the hidden numbers in turtle
indication = None     # A blank variable for later
start = None     # Record the start time
g_clock = 0       # Record the elapsed time
g_touch_body = 0     # Record the touch times
direction = None     # Record the last direction
one = None     # A blank variable for later
list_two = []     # A blank variable for later


# Create the screen, the border, and the initial introduction.
def create_screen():
    global g_screen, g_border, g_indication, g_introduction
    g_screen = turtle.Screen()
    g_screen.setup(600, 680, 0, 0)
    g_screen.tracer(False)

    g_border = turtle.Turtle()
    g_border.hideturtle()
    g_border.pensize(2)
    g_border.penup()
    g_border.goto(260, -300)
    g_border.pendown()
    g_border.setheading(90)
    g_border.forward(600)
    g_border.setheading(180)
    g_border.forward(520)
    g_border.setheading(270)
    g_border.forward(600)
    g_border.setheading(0)
    g_border.forward(520)
    g_border.penup()
    g_border.goto(260, 220)
    g_border.pendown()
    g_border.pensize(3)
    g_border.setheading(180)
    g_border.forward(520)

    g_indication = turtle.Turtle()
    g_indication.hideturtle()
    g_indication.penup()
    g_indication.goto(-200, 240)
    g_indication.write("Contact: "  + "0" + "   Time: " \
                       + "0" "   Motion: "+ "Paused" , font=("Arial", 16, "bold"))

    g_introduction = turtle.Turtle()
    g_introduction.penup()
    g_introduction.goto(-200, 120)
    g_introduction.hideturtle()
    g_introduction.write("Snake by Linda\nClick anywhere on the screen to start the game, have fun!!",
                         align="left", font=("Times", 13, "bold"))

    g_screen.update()


# Build the model to create the tail of the snake.
def create_one_tail_of_snake(x, y):
    one_part = turtle.Turtle()
    one_part.pensize(2)
    one_part.pencolor("blue")
    one_part.fillcolor("black")
    one_part.penup()
    one_part.goto(x, y)
    one_part.pendown()
    one_part.hideturtle()
    one_part.begin_fill()
    one_part.setheading(0)
    one_part.forward(20)
    one_part.setheading(270)
    one_part.forward(20)
    one_part.setheading(180)
    one_part.forward(20)
    one_part.setheading(90)
    one_part.forward(20)
    one_part.end_fill()
    turtle.update()
    return one_part


# Build the model to create the head of the snake.
def create_head_of_snake(x, y):
    one_part = turtle.Turtle()
    one_part.pensize(2)
    one_part.pencolor("red")
    one_part.fillcolor("red")
    one_part.penup()
    one_part.goto(x, y)
    one_part.pendown()
    one_part.hideturtle()
    one_part.begin_fill()
    one_part.setheading(0)
    one_part.forward(20)
    one_part.setheading(270)
    one_part.forward(20)
    one_part.setheading(180)
    one_part.forward(20)
    one_part.setheading(90)
    one_part.forward(20)
    one_part.end_fill()
    turtle.update()
    return one_part


# Create the initial monster
def create_initial_monster():
    global monster_x, monster_y, g_monster
    list_x = []
    list_y = []
    list_x.append(random.randrange(-248, -160, 20))
    list_x.append(random.randrange(140, 248, 20))
    monster_x = random.choice(list_x)
    list_y.append(random.randrange(-287, -180, 20))
    list_y.append(random.randrange(120, 208, 20))
    monster_y = random.choice(list_y)
    g_monster = turtle.Turtle("square")
    g_monster.color("yellow")
    g_monster.penup()
    g_monster.goto(monster_x, monster_y)


# Control the movement of the snake and finish the new indication, check to see if the food has been eaten, /
# and check whether win or not in this process.
def snake_move():
    global g_snake, g_direction, one, list_two
    change_indication()
    eat_number()
    win()
    if remain_or_not:
        if one == None:
            pass
        else:
            one.clear()
            for second in list_two:
                second.clear()
        if g_direction == 1:
            if g_snake[0][1] + 20 > 220:
                pass
            elif g_snake[0][1] + 20 == g_snake[1][1]:
                pass
            else:
                g_snake.insert(0, [g_snake[0][0], g_snake[0][1] + 20])
                g_snake.pop(-1)
        elif g_direction == 2:
            if g_snake[0][0] + 20 > 240:
                pass
            elif g_snake[0][0] + 20 == g_snake[1][0]:
                pass
            else:
                g_snake.insert(0, [g_snake[0][0] + 20, g_snake[0][1]])
                g_snake.pop(-1)
        elif g_direction == 3:
            if g_snake[0][1] - 20 < -280:
                pass
            elif g_snake[0][1] - 20 == g_snake[1][1]:
                pass
            else:
                g_snake.insert(0, [g_snake[0][0], g_snake[0][1] - 20])
                g_snake.pop(-1)
        elif g_direction == 4:
            if g_snake[0][0] - 20 < -260:
                pass
            elif g_snake[0][0] - 20 == g_snake[1][0]:
                pass
            else:
                g_snake.insert(0, [g_snake[0][0] - 20, g_snake[0][1]])
                g_snake.pop(-1)
        elif g_direction == 0:
            pass
        for each in range(len(g_snake) - 1, -1, -1):
            if each == 0:
                one = create_head_of_snake(g_snake[each][0], g_snake[each][1])
            else:
                two = create_one_tail_of_snake(g_snake[each][0], g_snake[each][1])
                list_two.append(two)
    else:
        return

    g_screen.ontimer(snake_move, 200)


# Snake extend its tail, and count the touch times.
def add_tail():
    global g_snake, g_direction, g_count, g_screen, add_or_not
    list_tail = []
    num = 0
    while add_or_not:
        change_indication()
        if len(g_snake) == 1:
            if g_direction == 1:
                if g_snake[0][1] + 20 > 220:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0], g_snake[0][1] + 20])
            elif g_direction == 2:
                if g_snake[0][0] + 20 > 240:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0] + 20, g_snake[0][1]])
            elif g_direction == 3:
                if g_snake[0][1] - 20 < -280:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0], g_snake[0][1] - 20])
            elif g_direction == 4:
                if g_snake[0][0] - 20 < -260:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0] - 20, g_snake[0][1]])
            elif g_direction == 0:
                pass
        else:
            if g_direction == 1:
                if g_snake[0][1] + 20 > 220:
                    pass
                elif g_snake[0][1] + 20 == g_snake[1][1]:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0], g_snake[0][1] + 20])
            elif g_direction == 2:
                if g_snake[0][0] + 20 > 240:
                    pass
                elif g_snake[0][0] + 20 == g_snake[1][0]:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0] + 20, g_snake[0][1]])
            elif g_direction == 3:
                if g_snake[0][1] - 20 < -280:
                    pass
                elif g_snake[0][1] - 20 == g_snake[1][1]:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0], g_snake[0][1] - 20])
            elif g_direction == 4:
                if g_snake[0][0] - 20 < -260:
                    pass
                elif g_snake[0][0] - 20 == g_snake[1][0]:
                    pass
                else:
                    num += 1
                    g_snake.insert(0, [g_snake[0][0] - 20, g_snake[0][1]])
            elif g_direction == 0:
                pass

        for each in range(len(g_snake) - 1, -1, -1):
            if each == 0:
                head = create_head_of_snake(g_snake[0][0], g_snake[0][1])
            else:
                tail = create_one_tail_of_snake(g_snake[each][0], g_snake[each][1])
                list_tail.append(tail)
        head.clear()
        for tail in list_tail:
            tail.clear()
        time.sleep(0.4)

        if num == g_count:
            add_or_not = False
        else:
            pass


# Generate random numbers and their coordinates
def create_random_number_and_their_position():
    global g_dic_position, dic_number_items
    for num in range(5):
        position_x = random.randrange(-260, 240, 20)
        position_y = random.randrange(-280, 220, 20)
        g_dic_position[num + 1] = [position_x, position_y]
        number = turtle.Turtle()
        number.penup()
        number.goto(position_x + 7, position_y - 17)
        number.write(num + 1, font=2)
        number.hideturtle()
        turtle.tracer(False)
        turtle.update()
        dic_number_items[num + 1] = number
    return dic_number_items


# Random hide and  make number appear.
def random_hide_and_appear():
    global hide, g_list_appear, g_list_appear_real, g_dic_position, g_hide, dic_number_items
    if len(g_list_appear_real) == 0:
        return
    else:
        if hide:
            lucky = random.choice(g_list_appear)
            g_list_appear.remove(lucky)
            dic_number_items[lucky].clear()
            g_hide.append(lucky)
            hide = False
        else:
            unlucky = g_hide[-1]
            g_hide.pop(-1)
            g_list_appear.append(unlucky)
            position = g_dic_position[unlucky]
            number = turtle.Turtle()
            number.penup()
            number.goto(position[0] + 7, position[1] - 17)
            number.write(unlucky, font=2)
            number.hideturtle()
            turtle.tracer(False)
            turtle.update()
            dic_number_items[unlucky] = number
            hide = True

    g_screen.ontimer(random_hide_and_appear, 5000)


# The monster moved toward the head of the snake.
def monster_move():
    global monster_x, monster_y, not_end, g_snake, g_monster, remain_or_not, g_screen, add_or_not, g_touch_body
    list_monster_move = []
    if not_end:
        for each in g_snake:
            if -10 < monster_x - each[0] < 30 and -30 < monster_y - each[1] < 10:
                g_touch_body += 1
                break
            else:
                pass
        g_monster.speed(2)
        if monster_x < g_snake[0][0] - 5:
            list_monster_move.append(1)
        elif monster_x > g_snake[0][0] + 5:
            list_monster_move.append(2)
        if monster_y < g_snake[0][1] - 5:
            list_monster_move.append(3)
        elif monster_y > g_snake[0][1] + 5:
            list_monster_move.append(4)
        if len(list_monster_move) == 0:
            not_end = False
            remain_or_not = False
            add_or_not = False
            lose_words = turtle.Turtle()
            lose_words.pencolor("red")
            lose_words.penup()
            lose_words.goto(g_snake[0][0], g_snake[0][1])
            lose_words.write("Game Over!!", font=2)
            lose_words.hideturtle()
            for i in range(len(g_snake)):
                if i == 0:
                    create_head_of_snake(g_snake[0][0], g_snake[0][1])
                else:
                    create_one_tail_of_snake(g_snake[i][0], g_snake[i][1])
            turtle.tracer(False)
            turtle.update()
        else:
            move = random.choice(list_monster_move)
            if move == 1:
                if 239 < monster_x < 248:
                    pass
                else:
                    monster_x += 10
                    g_monster.setheading(0)
                    g_monster.forward(10)
            elif move == 2:
                if -260 < monster_x < -239:
                    pass
                else:
                    monster_x -= 10
                    g_monster.setheading(180)
                    g_monster.forward(10)
            elif move == 3:
                if 205 < monster_y < 215:
                    pass
                else:
                    monster_y += 10
                    g_monster.setheading(90)
                    g_monster.forward(10)
            elif move == 4:
                if -340 < monster_y < -287:
                    pass
                else:
                    monster_y -= 10
                    g_monster.setheading(270)
                    g_monster.forward(10)
            if g_snake[0][0] - 5 < monster_x < g_snake[0][0] + 28 and g_snake[0][1] - 20 < monster_y < g_snake[0][1] + 5:
                not_end = False
                remain_or_not = False
                lose_words = turtle.Turtle()
                lose_words.pencolor("red")
                lose_words.penup()
                lose_words.goto(g_snake[0][0], g_snake[0][1])
                lose_words.write("Game Over!!", font=2)
                lose_words.hideturtle()
                for i in range(len(g_snake)):
                    if i == 0:
                        create_head_of_snake(g_snake[0][0], g_snake[0][1])
                    else:
                        create_one_tail_of_snake(g_snake[i][0], g_snake[i][1])
                turtle.tracer(False)
                turtle.update()

    g_screen.ontimer(monster_move, random.randint(200, 400))


# The function which begins this program
def begin(x, y):
    global g_introduction, g_direction, create_number, dic_number_items, start
    if -9000 < x < 9000:
        start = time.time()
        g_introduction.clear()
        g_direction = 1
        turtle.onkeypress(up, "Up")
        turtle.onkeypress(right, "Right")
        turtle.onkeypress(down, "Down")
        turtle.onkeypress(left, "Left")
        turtle.onkeypress(space, "space")
        turtle.listen()
        while create_number:
            dic_number_items = create_random_number_and_their_position()
            create_number = False

        monster_move()
        add_tail()
        first.clear()
        snake_move()
        random_hide_and_appear()


    else:
        pass


# Check to see if the snake has eaten the number
def eat_number():
    global g_snake, g_dic_position, g_count, dic_number_items, g_eat_how_many, g_list_appear, g_list_appear_real, add_or_not
    for i in g_list_appear:
        if g_snake[0] == g_dic_position[i]:
            g_list_appear.remove(i)
            g_list_appear_real.remove(i)
            dic_number_items[i].clear()
            g_count = i
            add_or_not = True
            add_tail()
            g_eat_how_many += 1
        else:
            pass


# Check to see if the player win or not.
def win():
    global g_eat_how_many, remain_or_not, not_end
    if g_eat_how_many == 5:
        remain_or_not = False
        not_end = False
        win_words = turtle.Turtle()
        win_words.pencolor("red")
        win_words.penup()
        win_words.goto(g_snake[0][0], g_snake[0][1])
        win_words.write("Winner!!", font=2)
        win_words.hideturtle()
        for i in range(len(g_snake)):
            if i == 0:
                create_head_of_snake(g_snake[0][0], g_snake[0][1])
            else:
                create_one_tail_of_snake(g_snake[i][0], g_snake[i][1])
        turtle.tracer(False)
        turtle.update()
    else:
        pass


# Change the motion, time, and count.
def change_indication():
    global g_direction, g_indication, start, g_clock, g_screen, g_touch_body, remain_or_not

    if remain_or_not:
        g_indication.clear()
        if g_direction == 1:
            motion = "Up"
        elif g_direction == 2:
            motion = "Right"
        elif g_direction == 3:
            motion = "Down"
        elif g_direction == 4:
            motion = "Left"
        else:
            motion = "Paused"

        end = time.time()
        if 0.7 <= end - start <= 1.3:
            start += 1
            g_clock += 1

        else:
            pass

        g_indication = turtle.Turtle()
        g_indication.hideturtle()
        g_indication.penup()
        g_indication.goto(-200, 240)
        g_indication.write("Contact: " + str(g_touch_body) + "   Time: " \
                           + str(g_clock) + "   Motion: " + motion, font=("Arial", 16, "bold"))
    else:
        return


# Receive the up key of the keyboard
def up():
    global g_direction
    g_direction = 1


# Receive the right key of the keyboard
def right():
    global g_direction
    g_direction = 2


# Receive the down key of the keyboard
def down():
    global g_direction
    g_direction = 3


# Receive the left key of the keyboard
def left():
    global g_direction
    g_direction = 4


# Receive the space key of the keyboard
def space():
    global g_direction, direction
    if g_direction == 0:
        g_direction = direction
    else:
        direction = g_direction
        g_direction = 0


# Use function
create_screen()
create_initial_monster()
first = create_head_of_snake(0, 0)
g_screen.onclick(begin)
turtle.mainloop()