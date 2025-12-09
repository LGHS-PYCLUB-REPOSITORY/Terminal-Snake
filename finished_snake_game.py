import time
import random
import logging

width = 15
height = 12
snake = [[5,5]]
velocity = [1,0]
apple = [9,6]
size = 0
LINES = 25
highscore = -1
RED = "\033[91m"
GREEN = "\033[92m"
LIME = "\033[32m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[0m"
block = ["[]","██"]
style = 1
torus = False
no_intersections = True

def new_apple(X,Y):
    global apple
    ## try apple placement
    for _ in range(1000):
        x = random.randint(0,width - 1)
        y = random.randint(0,height - 1)
        #print([x,y])
        if (not ([x,y] in snake)) and (not ((x == X) and (y == Y))):
            apple = [x,y]
            return
    logging.warning(RED+"Could not place apple")


def level(top):
    print(WHITE,end="")
    if style > -1: print(block[style],end="")
    else: print("//" if top else "\\\\",end="")
    for _ in range(width):
        ## print statement continues on one line
        if style > -1: print(block[style],end="")
        else: print("[]",end="")
    if style > -1: print(block[style],end="")
    else: print("\\\\" if top else "//",end="")
    print()

def draw():
    for _ in range(LINES):
        # to make the autoscroll work
        print()
    global size
    if size < 10:
        print(WHITE+"SCORE:"+BLUE,str(size),end="")
    else:
        print(WHITE+"SCORE:"+BLUE,size,end="")
    if highscore >= 0:
        print("    ")
        if highscore < 10:
            print(WHITE+"HIGHSCORE:"+BLUE,str(highscore))
        else:
            print(WHITE+"HIGHSCORE:"+BLUE,highscore)
    else: print()
    level(True)
    for y in range(height):
        if style > -1: print(WHITE+block[style],end="")
        else: print(WHITE+"||",end="")
        for x in range(width):
            if [x,y] in snake:
                if style > -1: print(BLUE+block[style],end="")
                else: print(WHITE+"()",end="")
            elif [x,y] == apple:
                if style > -1: print(RED+block[style],end="")
                else:
                    if size + 1 < 10:
                        print(WHITE+"0"+str(size + 1),end="")
                    else:
                        print(WHITE+str(size + 1),end="")
            elif [x,y-1] in snake or [x,y-1] == apple or y == 0:
                if style > -1: print(GREEN+block[style],end="")
                else: print("  ",end="")
            else:
              if style > -1: 
                if False:
                    print(GREEN+block[style],end="")
                else:
                    print(LIME+block[style],end="")
              else: print("  ",end="")
        if style > -1: print(WHITE+block[style],end="")
        else: print(WHITE+"||",end="")
        print()

    level(False)
    print()

def reset():
    global snake
    global apple
    global size
    global velocity
    snake = [[0,0]]
    apple = [5,5]
    size = 0
    velocity = [1,0]


def settings():
    while True:
        for _ in range(LINES):
            print()
        div = WHITE+" | "+WHITE
        global style
        global torus
        print(GREEN)
        print(" SNAKE GAME")
        #print(GREEN+"SNAKE GAME"+" - "+"AARUSH KALELE")
        #print(GREEN)
        print(CYAN+" BY AARUSH KALELE")
        #print(CYAN)
        #print(CYAN+" WITH PYTHON 3.17")
        print(BLUE)
        print(" [STYLE]")
        print()
        #print("             | BASIC | BOX | BLOCK |                    ")
        print(
            div,GREEN if style == -1 else RED,"BASIC",
            div,GREEN if style == 0 else RED,"BOX",
            div,GREEN if style == 1 else RED,"BLOCK",
            div,sep="")
        print(BLUE)
        print(" [WORLD]")
        print()
        #print("              | BOUNDED | INFINITE |                    ")
        print(
            div,GREEN if torus == False else RED,"BOUNDED",
            div,GREEN if torus == True else RED,"INFINITE",
            div,sep="")
        print(BLUE)
        print(" [SAVE]")
        print()
        #print("                      | S |                             ")
        print(div+GREEN+"S"+div)
        print()
        #print(BLUE+"[SAVE] ",div,"S",div,sep="")
        #print()
        #print(BLUE+"[EXIT] ",div,"E",div,sep="")
        #print()
        #exit()
        option = input()
        option = option.upper()
        match option:
            case "BASIC":
                style = -1
            case "BOX":
                style = 0
            case "BLOCK":
                style = 1
            case "BOUNDED":
                torus = False
            case "INFINITE":
                torus = True
            case "S":
                reset()
                return
        time.sleep(0)
    

def game_over():
    draw()
    global highscore
    global size
    highscore = size
    print(RED+"GAME OVER!"+WHITE)
    print("N = NEW GAME")
    print("E = EXIT NOW")
    print("S = SETTINGS")
    print("OPTION: ",end=YELLOW)
    option = input()
    option = option.upper()
    match option:
        case "E":
            print(GREEN+"THANKS FOR PLAYING!"+WHITE)
            exit()
        case "S":
            settings()
        case _:
            reset()
            ## game loop continues

def user_input():
    key = input()
    key = key.upper()
    global velocity
    global size
    match key:
        case "W":
            velocity = [0,-1]
        case "A":
            velocity = [-1,0]
        case "S":
            velocity = [0,1]
        case "D":
            velocity = [1,0]
        case "E" | "EXIT":
            draw()
            game_over()
            return
    #global snake
    #global size
    x = snake[-1][0] + velocity[0]
    y = snake[-1][1] + velocity[1]
    
    ## check apple
    if [x,y] == apple:
        new_apple(x,y)
        size += 1
    if len(snake) > size:
        snake.pop(0)

    ## check if hitting wall
    if not ((x in range(width)) and (y in range(height))):
        if torus == False:
            game_over()
            return
        else:
            ## torus mode
            if x >= width:
                x = 0
            if y >= height:
                y = 0
            if x < 0:
                x = width - 1
            if y < 0:
                y = height - 1
    
    ## check if intersection
    if no_intersections == True:
        if [x,y] in snake:
            game_over()
            return

    ## now we finally append the segment
    snake.append([x,y])

def main():
    draw()
    user_input()

def game_loop():
    while True:
        main()
        time.sleep(0)

print(CYAN+"\n\nWelcome to snake game!\n"+WHITE)
print("Enter WASD keys to move in any direction")
print("Enter no keys to continue in that direction")
print("Enter E to access the game menu\n")
print(CYAN+"Good luck, and try to get the highest score!\n")
print(WHITE+"Press any key to continue\n")
input()

game_loop()
