import random

def win(table, player):
    if table[0] == table[1] == table[2] == player or \
        table[3] == table[4] == table[5] == player or \
        table[6] == table[7] == table[8] == player or \
        table[0] == table[3] == table[6] == player or \
        table[1] == table[4] == table[7] == player or \
        table[2] == table[5] == table[8] == player or \
        table[0] == table[4] == table[8] == player or \
        table[2] == table[4] == table[6] == player:
            return True
    else: 
        return False
       
def Drawn (table):
    for i in table:
        if i == " ":
            return False    
    return True

def avalableMove(table, place):
    return table[place] == " "

def playerMove(table, snd):
    positions = ["1","2","3","4","5","6","7","8","9"]
    position = None
    while True:
        if position not in positions:
            position = snd
        else:
            position = int(position)
            if not avalableMove(table, position-1):
                print("ERRO::MOVE NO AVALIABLE")
            else:
                return position-1
def inteligentMoves(table, thinker, adversary):
    for i in range(9):
        copy = list(table)
        if avalableMove(copy, i):
            copy[i] = thinker
            if win(copy, thinker):
                return i
            
    for i in range(9):
        copy = list(table)
        if avalableMove(copy, i):
            copy[i] = adversary
            if win(copy, adversary):
                return i
            
    if thinker == "X":
        if table[4]==" ":
            return 4
        elif table[0]== " " or table[2]== " " or table[6]== " " or table[8]== " " :
            void = []
            for i in [0,2,6,8]:
                if table[i] == " ":
                    void.append(i)
            return random.choice(void)
        else:
            void = []
            for i in [1,3,5,7]:
                if table[i] == " ":
                    void.append(i)
                    print (void)
            return random.choice(void)
        
    if thinker == "O":
        counter = 0
        for i in range(9):
            if table[i] == " ":
                counter += 1
        if counter == 7:
            if table[4]==" ":
                return 4
        
    while True:
        square = random.randint(0,8)
        if not avalableMove(table, square):
            square = random.randint(0,8)
        else:
            return square
        
#Declacaracion de estados inicales 


