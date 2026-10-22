map = [["x",".",".","x"],["x",".","T","x"],["x","T",".","x"]]
print("Welcome to the Treasure Hunt Game! You are represented by 'P' and your goal is to reach the treasure 'T' by moving through the map. You can move up (w), down (s), left (a), or right (d). Good luck!🪎")
print("Shown below is the map. 'x' represents walls, '.' represents open paths, and 'T' represents the treasure. You start at the top left corner of the map.")
for i in map:
    print(*i)
x_pos = 0
y_pos = 0
map[y_pos][x_pos] = "P"
def move_up(): 
    global x_pos, y_pos
    if y_pos > 0 and map[y_pos-1][x_pos] != "x":
        map[y_pos][x_pos] = "."
        y_pos -= 1
        map[y_pos][x_pos] = "P"
        print("This is the current map:")
        for i in map:
            print(*i)
    else:
        print("You can't move in this direction!")
def move_down():
    global x_pos, y_pos
    if y_pos < 2 and map[y_pos+1][x_pos] != "x":
        map[y_pos][x_pos] = "."
        y_pos += 1
        map[y_pos][x_pos] = "P"
        print("This is the current map:")
        for i in map:
            print(*i)
    else:
        print("You can't move in this direction!")   
def move_left():
    global x_pos, y_pos
    if x_pos > 0 and map[y_pos][x_pos-1] != "x":
        map[y_pos][x_pos] = "."
        x_pos -= 1
        map[y_pos][x_pos] = "P"
        print("This is the current map:")
        for i in map:
            print(*i)
    else:
        print("You can't move in this direction!") 
def move_right():
    global x_pos, y_pos
    if x_pos < 3 and map[y_pos][x_pos+1] != "x":
        map[y_pos][x_pos] = "."
        x_pos += 1
        map[y_pos][x_pos] = "P"
        print("This is the current map:")
        for i in map:
            print(*i)
    else:
        print("You can't move in this direction!")
while map[y_pos][x_pos] != map[1][2] and map[y_pos][x_pos] != map[2][1]:
    direction = input("Enter direction you want to move (w/a/s/d):").lower()
    if direction == "w":
        move_up()
    elif direction == "s":
        move_down()
    elif direction == "a":
        move_left()
    elif direction == "d":
        move_right()
print("Congratulations! You found the treasure! 🏆")

