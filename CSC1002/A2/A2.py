import turtle

turtle.colormode(255)
list_use = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
turn = 1
line = 0
row = 999
which_connect = 0
check_0_exist = False
event_processing = False
border = 0
line_start = 999
tie_or_not = 0
count_maybe_1 = []
count_maybe_2 = []
count_maybe_3 = []
count_maybe_4 = []
count_1 = 0
count_2 = 0


# Draw the Column Trackers
def draw_tracker(count, x, y):
    low_tracker = turtle.Turtle("blank")
    low_tracker.color(0, 0, 0)
    low_tracker.fillcolor(0, 0, 0)
    if count > 8:
        return
    low_tracker.hideturtle()
    low_tracker.penup()
    low_tracker.goto(x, y)
    low_tracker.pendown()
    low_tracker.seth(0)
    low_tracker.begin_fill()
    low_tracker.forward(60)
    low_tracker.right(90)
    low_tracker.forward(20)
    low_tracker.right(90)
    low_tracker.forward(60)
    low_tracker.right(90)
    low_tracker.forward(20)
    low_tracker.end_fill()
    draw_tracker(count + 1, x + 70, y)


# Draw a signal circle
def draw_circle(x, y, color : tuple):
    each_circle = turtle.Turtle("blank")
    each_circle.color(color)
    each_circle.fillcolor(color)
    each_circle.hideturtle()
    each_circle.penup()
    each_circle.goto(x, y)
    each_circle.pendown()
    each_circle.seth(0)
    each_circle.begin_fill()
    each_circle.circle(30)
    each_circle.end_fill()


# Draw the edges of the column trackers if the mouse is waiting in the special area.
def draw_edge(event):
    x = event.x
    y = event.y
    global turn
    if turn == 1:
        color = (0, 0, 255)
    else:
        color = (255, 0, 0)
    edge = turtle.Turtle("blank")
    for edge_draw_num in range(9):
        if 25 + edge_draw_num * 70 < x < 85 + edge_draw_num * 70:
            edge.color(color)
            edge.pensize(5)
            edge.hideturtle()
            edge.penup()
            edge.goto(-275 + 70 * edge_draw_num, -305)
            edge.pendown()
            edge.seth(0)
            edge.forward(60)
            edge.right(90)
            edge.forward(20)
            edge.right(90)
            edge.forward(60)
            edge.right(90)
            edge.forward(20)
        else:
            edge.color(255, 255, 255)
            edge.pensize(5)
            edge.hideturtle()
            edge.penup()
            edge.goto(-275 + 70 * edge_draw_num, -305)
            edge.pendown()
            edge.seth(0)
            edge.forward(60)
            edge.right(90)
            edge.forward(20)
            edge.right(90)
            edge.forward(60)
            edge.right(90)
            edge.forward(20)


# Check where the mouse is and record.
def coordinate(x,y):
    global line
    global border
    global event_processing

    if turn == 1:
        color = (0, 0, 255)
    else:
        color = (255, 0, 0)

    if event_processing:
        return

    event_processing = True

    if -275 < x < -215:
        line = 0
        record_input()
        if row < 8:
            draw_circle(-245, 205 - row * 70, color)
            border = -245
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif -205 < x < -145:
        line = 1
        record_input()
        if row < 8:
            draw_circle(-175, 205 - row * 70, color)
            border = -175
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif -135 < x < -75:
        line = 2
        record_input()
        if row < 8:
            draw_circle(-105, 205 - row * 70, color)
            border = -105
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif -65 < x < -5:
        line = 3
        record_input()
        if row < 8:
            draw_circle(-35, 205 - row * 70, color)
            border = -35
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif 5 < x < 65:
        line = 4
        record_input()
        if row < 8:
            draw_circle(35, 205 - row * 70, color)
            border = 35
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif 75 < x < 135:
        line = 5
        record_input()
        if row < 8:
            draw_circle(105, 205 - row * 70, color)
            border = 105
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif 145 < x < 205:
        line = 6
        record_input()
        if row < 8:
            draw_circle(175, 205 - row * 70, color)
            border = 175
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    elif 215 < x < 275:
        line = 7
        record_input()
        if row < 8:
            draw_circle(245, 205 - row * 70, color)
            border = 245
            check_horizontal()
            check_oblique()
            check_vertical()
            change_player()
            borders_circles()
        else:
            pass

    title()
    event_processing = False


# Recorde the input.
def record_input():
    global line
    check_input = True
    while check_input:
        global turn
        global row
        for row in range(7, -1, -1):
            if list_use[row][line] == 0:
                list_use[row][line] = turn
                check_input = False
                break
            else:
                pass
        else:
            row = 8
            check_input = False


# Determine whether vertical direction satisfies the condition
def check_vertical():
    global row
    global line
    if row < 5:
        for row_before in range(1, 4):
            if list_use[row + row_before][line] != list_use[row][line]:
                break
        else:
            scr.title(f"Winner ! Player {turn}")
            global which_connect
            which_connect = 1
    else:
        pass


# Determine whether horizontal direction satisfies the condition
def check_horizontal():
    global row
    global which_connect
    if list_use[row].count(turn) < 4:
        pass
    else:
        global line_start
        for line_start in range(0, 5):
            for line_each in range(4):
                if list_use[row][line_start + line_each] != turn:
                    break
            else:
                scr.title(f"Winner ! Player {turn}")
                which_connect = 2
                break


# Determine whether oblique direction satisfies the condition
def check_oblique():
    global row
    global line
    global count_maybe_1
    global count_maybe_2
    global count_maybe_3
    global count_maybe_4
    global count_1
    global count_2

    for difference in range(1, 4):
        if row - difference >= 0 and line - difference >= 0:
            if list_use[row - difference][line - difference] != turn:
                break
            else:
                global count_maybe_1
                count_maybe_1.append(difference)
                count_1 += 1
        else:
            break

    for difference in range(1, 4):
        try:
            if list_use[row + difference][line + difference] != turn:
                break
            else:
                global count_maybe_2
                count_maybe_2.append(difference)
                count_1 += 1
        except:
            break

    for difference in range(1, 4):
        if line - difference >= 0:
            try:
                if list_use[row + difference][line - difference] != turn:
                    break
                else:
                    global count_maybe_3
                    count_maybe_3.append(difference)
                    count_2 += 1
            except:
                break
        else:
            break

    for difference in range(1, 4):
        if row - difference >= 0:
            try:
                if list_use[row - difference][line + difference] != turn:
                    break
                else:
                    global count_maybe_4
                    count_maybe_4.append(difference)
                    count_2 += 1
            except:
                break
        else:
            pass

    if count_1 == 3 or count_2 == 3:
        scr.title(f"Winner ! Player {turn}")
        global which_connect
        which_connect = 3
    else:
        count_1 = 0
        count_2 = 0
        count_maybe_1 = []
        count_maybe_2 = []
        count_maybe_3 = []
        count_maybe_4 = []


# Change the player
def change_player():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1


# Determine the title of the game.
def title():
    global check_0_exist
    global tie_or_not
    for first_list in range(8):
        for second_list in list_use[first_list]:
            if second_list == 0:
                check_0_exist = True
            else:
                pass
    if check_0_exist:
        if turn == 1:
            scr.title("CONNECT 4 - Player 1 Turn")
        elif turn == 2:
            scr.title("CONNECT 4 - Player 2 Turn")
        check_0_exist = False
    elif tie_or_not != 0:
        pass
    else:
        turtle.title("Game Tied ! ")


# Draw the border of the circles which connect-four.
def borders_circles():
    color = (0, 255, 0)
    global which_connect
    global border
    global row
    global tie_or_not
    draw_border = turtle.Turtle("blank")
    draw_border.color(color)
    draw_border.width(5)
    if which_connect == 1:
        which_connect = 0
        tie_or_not = 1
        for i in range(4):
            draw_border.penup()
            draw_border.goto(border, 205 - ( row + i ) * 70)
            draw_border.pendown()
            draw_border.circle(30)
            turtle.update()

    elif which_connect == 2:
        which_connect = 0
        tie_or_not = 1
        global line_start
        for i in range(4):
            draw_border.penup()
            draw_border.goto(-245 + 70 * ( line_start + i ), 205 - row * 70)
            draw_border.pendown()
            draw_border.circle(30)
            turtle.update()

    elif which_connect == 3:
        which_connect = 0
        tie_or_not = 1
        global count_maybe_1
        global count_maybe_2
        global count_maybe_3
        global count_maybe_4
        global count_1
        global count_2
        draw_border.penup()
        draw_border.goto(border, 205 - row * 70)
        draw_border.pendown()
        draw_border.circle(30)

        if count_1 == 3:
            if count_maybe_1 != []:
                for i in count_maybe_1:
                    draw_border.penup()
                    draw_border.goto(border - 70 * i, 205 - (row - i) * 70)
                    draw_border.pendown()
                    draw_border.circle(30)
                    turtle.update()
            else:
                pass
            if count_maybe_2 != []:
                for i in count_maybe_2:
                    draw_border.penup()
                    draw_border.goto(border + 70 * i, 205 - (row + i) * 70)
                    draw_border.pendown()
                    draw_border.circle(30)
                    turtle.update()
            else:
                pass

        elif count_2 == 3:
            if count_maybe_3 != []:
                for i in count_maybe_3:
                    draw_border.penup()
                    draw_border.goto(border - 70 * i, 205 - (row + i) * 70)
                    draw_border.pendown()
                    draw_border.circle(30)
                    turtle.update()
            else:
                pass
            if count_maybe_4 != []:
                for i in count_maybe_4:
                    draw_border.penup()
                    draw_border.goto(border + 70 * i, 205 - (row - i) * 70)
                    draw_border.pendown()
                    draw_border.circle(30)
                    turtle.update()
            else:
                pass
        else:
            pass
        count_1 = 0
        count_2 = 0
        count_maybe_1 = []
        count_maybe_2 = []
        count_maybe_3 = []
        count_maybe_4 = []


turtle.tracer(False)
turtle.setup(600, 670, 0, 0)
draw_tracker(1, -275, -305)
turtle.title("CONNECT 4 - Player 1 Turn")
scr = turtle.Screen()
follow = scr.getcanvas()
follow.bind("<Motion>", draw_edge)
scr.onclick(coordinate)
turtle.done()