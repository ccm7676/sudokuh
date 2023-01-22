import generate
import levels

def main():
    #run generate function until it generates a functioning sudoku puzzle
    puzzle = False
    while puzzle == False:
        puzzle = generate.generate()

    levels.easy(puzzle)



if __name__ == "__main__":
    main()

