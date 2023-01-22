import random

#puzzle grid
puzzle = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1]]


#display the puzzle in terminal
def show(sodoku):

    #loop through puzzle
    for row in puzzle:
        for box in row:

            #check if -1 and print empty
            if box == -1:
                print(" |", end="")

            #print num in box
            else:
                print(str(box) + "|",end="")
        print("\n")


#get all values in 3x3 box for specific coordinate
def get_box(y,x,puzzle):
    xbox = 0
    ybox = 0

    #get vertical box 
    if x < 3:
        xbox = 0
    elif x < 6:
        xbox = 3
    elif x < 9:
        xbox = 6
    
    #get horizontal box
    if y < 3:
        ybox = 0
    elif y < 6:
        ybox = 3
    elif y < 9:
        ybox = 6



    result = [puzzle[ybox][xbox],puzzle[ybox][xbox + 1],puzzle[ybox][xbox + 2], puzzle[ybox + 1][xbox],puzzle[ybox +1][xbox +1],puzzle[ybox +1][xbox +2],puzzle[ybox +2][xbox],puzzle[ybox+2][xbox+1],puzzle[ybox+2][xbox+2]]
    #returns values for each box in the 3x3
    return result

#check for all possible number for one box
def is_possible(y,x,puzzle):

    #list that will be returned
    possible = [1,2,3,4,5,6,7,8,9]
    
    #a loop from one to nine used for rows and collumns
    for i in range(9):

        #coll
        num = puzzle[y][i]
        #row
        num2 = puzzle[i][x]
        
        #check if number isn't -1 and is part of the possible array and removes it from the array
        if num != -1 and num in possible:
            possible.remove(num)

        if num2 != -1 and num2 in possible:
            possible.remove(num2)
    
    #loops through all values in current 3x3
    for box in get_box(y,x,puzzle):

        if box != -1 and box in possible:
            possible.remove(box)

    return possible

        
#function that uses the other functions to generate a full sudoku puzzle
def generate():
    global puzzle
    puzzle  = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    #loops through rows and collumns of puzzle and run the is_possible function on each square
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            try:
                puzzle[i][j] = random.choice(is_possible(i,j,puzzle))
            except:
                return False
    return puzzle


