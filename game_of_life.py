import random, os, time

#square layout
size = 50
layout = [[random.choice((" ",0)) for j in range(size)] for i in range(size)]

#get the neighbors of a cell
def neighbors(row, col, status):
    if status:
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i != row or j != col:
                    yield (i,j)

#loops over layout once to record the necessary changes, again to apply them
def step():
    signals_dict = {}
    #if a cell alive, its neighbors get added to singnal_dict with a value of 1
    #if a neighbor is already in the dict, their value is increased by 1
    #dict is an index of how many alive neighbors a cell has
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

    #if a living cell has more than 3 living neighbors, it dies
    #if a living cell has less than 2 living neighbors, it dies
    #if a dead cell has 3 neighbors, it becomes alive
    #loop through each cell and and make changes based on signal_dict
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

#prints the current layout, waits 1 second, clears the console, repeats 
while 1:
    start = time.time()
    print(" ".join("#"*size))
    print("\n".join([" ".join([str(i) for i in row]) for row in layout]))
    print(" ".join("#"*size))
    step()
    wait = 1-(time.time()-start)
    if wait <= 1:
        time.sleep(wait)
    os.system('cls' if os.name == 'nt' else 'clear')
