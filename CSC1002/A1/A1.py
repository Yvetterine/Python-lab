import random

global size_each
global list_use
global left
global right
global up
global down
global list_direction_letters_only


# 1.We convert signs of the size to the real sizes to  conveniently use them.
# 2. Make the program to delete the wrong input.
def input_size():
    kind = input("Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game: ")
    check_input = True
    while check_input:
        global size_each
        if kind == "1":
            check_input = False
            size_each = 3
        elif kind == "2":
            check_input = False
            size_each = 4
        elif kind == "q":
            check_input = False
            size_each = "q"
        else:
            kind = input("Please input 1 or 2 or q again: ")


# Find the number of inversion numbers in a list(using in the initial puzzle)
def find_inversion_number(list_initial, size_each):
    count = 0
    for fir in range(size_each ^ 2):
        if list_initial[fir] == "  ":
            pass
        else:
            for sec in range(fir, size_each ^ 2):
                if list_initial[sec] == "  ":
                    pass
                else:
                    if list_initial[fir] > list_initial[sec]:
                        count += 1
                    else:
                        pass
    return count


# Give an initial puzzle which could be solved.
# In this part, I follow some mathematical theory about which sliding puzzles are solvable.
# If you are interested about that, please check https://www.jianshu.com/p/1c1849d876b2
def initial():
    input_size()
    if size_each == 3:
        list_initial = [1, 2, 3, 4, 5, 6, 7, 8, "  "]
        initial_check = True
        while initial_check:  # Check the random initial puzzle whether it is solvable.
            random.shuffle(list_initial)
            count = find_inversion_number(list_initial, size_each)
            if count % 2 == 0:
                list_use = [[], [], []]
                for row in range(3):
                    for line in range(3):
                        list_use[row].append(list_initial[0])
                        list_initial.pop(0)
                output(list_use)
                return list_use  # If this puzzle is solvable, go on.
            else:
                pass  # If this puzzle is not solvable, return and create a new one.
    elif size_each == 4:
        list_initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, "  "]
        initial_check = True
        while initial_check:
            random.shuffle(list_initial)
            zero_num = list_initial.index("  ")
            zero_first_appear_row = zero_num // 4
            count = find_inversion_number(list_initial,size_each)
            if count % 2 == 0:
                if (3 - zero_first_appear_row) % 2 == 0:
                    list_use = [[], [], [], []]
                    for row in range(4):
                        for line in range(4):
                            list_use[row].append(list_initial[0])
                            list_initial.pop(0)
                    output(list_use)
                    return list_use
                else:
                    pass
            else:
                if (3 - zero_first_appear_row) % 2 != 0:
                    list_use = [[], [], [], []]
                    for row in range(4):
                        for line in range(4):
                            list_use[row].append(list_initial[0])
                            list_initial.pop(0)
                    output(list_use)
                    return list_use
                else:
                    pass
    elif size_each == "q":
        print("Goodbye! ")
        return "q"


#  Find the location of the empty
def find_empty(list_use):
    for row in range(size_each):
        for line in range(size_each):
            if list_use[row][line] == "  ":
                return row, line


# We relate directions to the letters users input as well as delete the wrong input.
def input_letters():
    check = True
    while check:
        info = input("Please enter the four letters used for left, right, up and down move(No space is required):")
        if info.isalpha():  # Check whether the input is both letters
            info = info.upper()
            list_letters = []
            for i in info:
                list_letters.append(i)
            if len(list_letters) != 4:     # Check whether the number of input letters is 4
                print("Wrong number letters! Please enter the four letters again!")
            else:
                list_ascll = []
                for i in list_letters:
                    letters_ascll = ord(i)
                    list_ascll.append(letters_ascll)
                for i in range(3):
                    if list_ascll[i] == list_ascll[i + 1]:     # Check whether the input letters are the same.
                        print("Same letters! Please enter the different letters again!")
                        break
                else:
                    global left
                    global right
                    global up
                    global down
                    left = list_letters[0]
                    right = list_letters[1]
                    up = list_letters[2]
                    down = list_letters[3]
                    check = False  # When the input is wrong, let the users input again.
        else:
            print("Non-letter!Please enter letters again!")


# According to the location of the empty, procedure will give appropriate suggest to help users to do the decision,
# and from this step, procedure will get the order from users
def order(list_use):
    list_direction = ["left-" + left, "right-" + right, "up-" + up, "down-" + down]
    global list_direction_letters_only
    list_direction_letters_only = [left, right, up, down]
    row, line = find_empty(list_use)
    if row - 1 < 0:                                                    # Some special locations of the empty.
        list_direction.remove("down-" + down)
        list_direction_letters_only.remove(down)
    elif row + 1 == size_each:
        list_direction.remove("up-" + up)
        list_direction_letters_only.remove(up)
    if line - 1 < 0:
        list_direction.remove("right-" + right)
        list_direction_letters_only.remove(right)
    elif line + 1 == size_each:
        list_direction.remove("left-" + left)
        list_direction_letters_only.remove(left)
    if len(list_direction) == 2:
        demand = input(f"Enter your move ({list_direction[0]}, {list_direction[1]}) :")  # Give users hint
    elif len(list_direction) == 3:
        demand = input(f"Enter your move ({list_direction[0]}, {list_direction[1]}, {list_direction[2]}) :")
    else:
        demand = input(f"Enter your move ({list_direction[0]}, {list_direction[1]}, {list_direction[2]}, {list_direction[3]}) :")
    return demand, row, line


# In this step, the procedure will convert the order to the computer language, preparing for the next step.
def bridge_between_move_and_order(list_use):  # Relate the order to the real operation.
    demand, row, line = order(list_use)
    if demand.upper() in list_direction_letters_only:
        if demand.upper() == left:
            move_left_or_right(list_use, row, line, num=1)
        elif demand.upper() == right:
            move_left_or_right(list_use, row, line, num=-1)
        elif demand.upper() == up:
            move_up_or_down(list_use, row, line, num=1)
        elif demand.upper() == down:
            move_up_or_down(list_use, row, line, num=-1)
        output(list_use)
    else:
        print("Please input a letter which is in the tip")


# Operate the order in realty if the requested direction is left or right.
def move_left_or_right(list_use, row, line, num):
    list_use[row][line] = list_use[row][line + num]
    list_use[row][line + num] = "  "


# Operate the order in realty if the requested direction is up or down.
def move_up_or_down(list_use, row, line, num):
    list_use[row][line] = list_use[row + num][line]
    list_use[row + num][line] = "  "


# Convert the output from a list to an array.
def output(list_use):
    for row in range(size_each):
        for line in range(size_each):
            if list_use[row][line] == "  ":
                print("%-3s\t" % "    ", end=" ")
            else:
                print("%-3s\t" % list_use[row][line], end=" ")
        print(end="\n")


# The main body
def check_finish():
    print("Welcome to Linda’s puzzle game! This is an interactive sliding puzzle game."
          " The objective of the game is to re-arrange the tiles into a sequential order by their numbers"
          "(left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down). "
          " Please follow the hints the game offers. Hope you have a good time!")
    big_check = True
    while big_check:
        input_letters()
        list_use = initial()
        if list_use == "q":
            break
        move = 0
        check = True
        while check:
            if list_use == [[1, 2, 3], [4, 5, 6], [7, 8, "  "]] or list_use == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, "  "]]:
                print(f"Congratulations! You solved the puzzle in {move} moves!")
                check = False
                continue_or_not = input(f"If you want to continue another game, please input 'c',  "
                                        f"or if you want to stop, please input 's' :  ")
                small_check = True
                while small_check:  # Check whether the input is s or c.
                    if continue_or_not.lower() != "s" and continue_or_not.lower() != "c":
                        continue_or_not = input("Please input 'c' or 's' : ")
                        continue
                    else:
                        small_check = False
                if continue_or_not.lower() == "s":
                    print("Goodbye! ")
                    big_check = False
                else:
                    pass
            else:
                move += 1
                bridge_between_move_and_order(list_use)


check_finish()