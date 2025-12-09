import random
snake = [[0,0]]
WIDTH = 10
HEIGHT = 10
apple = [4,4]

def process():
    direction = input().upper()
    move_y = 0
    move_x = 0
    global apple
    match direction:
        case "W":
            move_y -= 1
        case "A":
            move_x -= 1
        case "S":
            move_y += 1
        case "D":
            move_x += 1

    new = [snake[-1][0] + move_x, 
           snake[-1][1] + move_y]
    if new in snake: exit()
    snake.append(new)
    if apple in snake: 
        apple = [random.randint(0,WIDTH - 1),
                 random.randint(0,HEIGHT - 1)]
    else: snake.pop(0)

def draw():
    # Look up "terminal color codes"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    for y in range(0,HEIGHT):
        for x in range(0,WIDTH):
            if [x,y] in snake:
                print(BLUE + "██",end="")
            elif [x,y] == apple:
                print(RED + "██",end="")
            else:
                print(GREEN+"██",end="")
        print()

while True:
    # add enough lines to hide the last display printed
    for i in range(20): print()
    draw()
    process()