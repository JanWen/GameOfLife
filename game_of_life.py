import random, os, time

#layout is square
size = 50
layout = [[random.choice((" ",0)) for j in range(size)] for i in range(size)]

#get the neighbors of a cell
def neighbors(row, col, status):
    if status:
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i != row or j != col:
                    yield (i,j)

#Loops over layout once to record the necessary changes, once to apply them
def step():
    signals_dict = {}
    #If a cell alive, it's neighbors get added singnal_dict with a value of 1
    #if a neighbor is already in the dict, their value get increased by 1
    #Ends up being index of how many alive neighbors a cell has
    current_row = 0
    for row in layout:
        current_col = 0
        for cell in row:
            for sig in neighbors(current_row,current_col,cell):
                if sig not in signals_dict:
                    signals_dict[sig] = 1
                else: signals_dict[sig] += 1
            current_col += 1
        current_row += 1
    
    #Loop through each cell and and make changes based on signal_dict
    current_row = 0
    for row in layout:
        current_col = 0
        for cell in row:
            pos = (current_row, current_col)
            if pos in signals_dict:
                signal = signals_dict[pos]
            else: signal = 0
            if cell and (signal < 2 or signal > 3):
                    layout[pos[0]][pos[1]] = 0
            elif not cell and signal == 3:
                    layout[pos[0]][pos[1]] = " "
            current_col += 1
        current_row += 1

#Prints the current layout, waits 1 second, clears the console, repeats 
while 1:
    start = time.time()
    print("#"*size*2)
    print("\n".join([" ".join([str(i) for i in row]) for row in layout]))
    print("#"*size*2)
    step()
    wait = 1-(time.time()-start)
    if wait <= 1:
        time.sleep(wait)
    os.system('cls' if os.name == 'nt' else 'clear')
