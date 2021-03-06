import time, socket, sys

board_color = color(245, 218, 129)
board_height = 0
board_width = 0
height_unit = 0
width_unit = 0
isPushed = False
turn_id = 0
board = 0
isGameEnabled = False
isServer = True
count = 0
max_count = 0

def initBoard(height_n, width_n):
    fill(board_color)
    rect(0, 0, 800, 800)
    
    global board_width
    global board_height
    global height_unit
    global width_unit
    
    global max_count
    
    max_count = width_n * height_n
    board_width = width_n
    board_height = height_n
    
    height_unit = 800 / height_n
    width_unit = 800 / width_n
    
    for i in range(height_n):
        line(0, height_unit * i, 799, height_unit * i)
        
    for j in range(width_n):
        line(width_unit * j, 0, width_unit * j, 799)
        
def player_turn(i, j, pid):
    global turn_id
    global isGameEnabled
    global count
    global max_count
    
    if isCanPut(i, j):
        board[i][j] = pid
        draw_piece(i, j, pid)
        count += 1
        turn_id = 1 - pid
        
        if turn_id == 0: s1 = "Black's turn"
        elif turn_id == 1: s1 = "White's turn"
        print_text(s1)

        judgement = Judge(board, i, j, pid)
        if count == max_count:
            print_text("Draw")
            isGameEnabled = False
        elif judgement == 1:
            if pid == 0:
                s1 = "Black"
            elif pid == 1:
                s1 = "White"

            print_text(s1 + " won")
            isGameEnabled = False
    else:
        print_text("Cannot put a piece on the position")

def Judge(b, y, x, pid):
    base_x = x - 3
    base_y = y
    while base_x <= x:
        count = 0
        for dx in range(4):
            now_x = base_x + dx
            if 0 <= now_x < board_width:
                if board[base_y][now_x] == pid:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return 1
        base_x += 1 

    base_x = x
    base_y = y - 3
    while base_y <= y:
        count = 0
        for dy in range(4):
            now_y = base_y + dy
            if 0 <= now_y < board_height:
                if board[now_y][base_x] == pid:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return 1
        base_y += 1 

    base_x = x - 3
    base_y = y + 3
    while base_y >= y and base_x <= x:
        count = 0
        for dxy in range(4):
            now_y = base_y - dxy
            now_x = base_x + dxy
            if (0 <= now_y < board_height) and (0 <= now_x < board_width):
                if board[now_y][now_x] == pid:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return 1
        base_x += 1
        base_y -= 1

    base_x = x - 3
    base_y = y - 3
    while base_y <= y and base_x <= x:
        count = 0
        for dxy in range(4):
            now_y = base_y + dxy
            now_x = base_x + dxy
            if (0 <= now_y < board_height) and (0 <= now_x < board_width):
                if board[now_y][now_x] == pid:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return 1
        base_x += 1
        base_y += 1

    i = 0
    j = 0
    isContainSpace = False
    
    while i < board_height:
        while j < board_width:
            if board[i][j] == 2:
                isContainSpace = True
            j += 1
        i += 1
    
    if not isContainSpace:
        return 0

    return 2

def isCanPut(y, x):
    if not ((0 <= y < board_height) and (0 <= x < board_width)):
        return False

    if board[y][x] != 2:
        return False

    down_flg = True
    left_flg = True

    i = y + 1
    j = x

    while i < board_height:
        if board[i][j] == 2:
           down_flg = False
        i += 1

    i = y
    j = x - 1

    while 0 <= j:
        if board[i][j] == 2:
            left_flg = False
        j -= 1

    canFlg = left_flg or down_flg

    return canFlg
      
def draw_piece(i, j, pid):
    draw_space(i, j)
    noStroke()
    colour = pid * 255
    fill(colour)
    ellipse((width_unit * j + width_unit * (j + 1)) / 2, (height_unit * i + width_unit * (i + 1)) / 2, width_unit * 0.8, height_unit * 0.8)

def draw_space(i, j):
    noStroke()
    fill(board_color)
    rect(width_unit * j + 1, height_unit * i + 1, width_unit - 1, height_unit - 1)
    
def clickScreen(y, x, pid):
    if 0 < x < 800 and 0 < y < 800:
        global height_unit
        global width_unit
            
        i = y // height_unit
        j = x // width_unit
        
        player_turn(i, j, pid)
        
def startGame():
    initBoard(10, 10)
    global board
    global isGameEnabled
    board = [[2 for i in range(board_width)] for j in range(board_width)]
    print_text("Black's turn")
    stroke(0)
    line(0, 902, 800, 902)
    isGameEnabled = True
    
def print_text(s1):
    fill(255)
    stroke(255)
    rect(0, 801, 800, 100)

    if s1 == "Black won" or s1 == "White won" or s1 == "Draw":
        fill(255, 0, 0)
    else:
        fill(0)
    textSize(40)
    text(s1, 50, 825, 99999, 99999)
    
def print_text2(s1):
    fill(0, 0, 255)
    textSize(20)
    text(s1, 10, 970, 99999, 99999)

def setup():
    size(800, 1000)
    background(255)
    startGame()

def draw():
    if isGameEnabled:
        global isPushed
        global turn_id
        if mousePressed and not isPushed:
            isPushed = True
            clickScreen(mouseY, mouseX, turn_id)
        elif not mousePressed and isPushed:
            isPushed = False
