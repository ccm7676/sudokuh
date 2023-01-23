import generate
import levels
import menu
import gameui

def main():
    if menu.show() == "play":
        play();
    elif menu.show() == "settings":
        print("settings")

def play():
    #run generate function until it generates a functioning sudoku puzzle
    solution = False
    while solution == False:
        solution = generate.generate()

    puzzle = levels.easy(solution)
    gameui.show(puzzle,solution)



if __name__ == "__main__":
    main()

