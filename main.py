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
    solution = 0
    while solution == 0:
        solution = generate.generate()
    
    solution2 = str(solution)
    print(solution2)
    puzzle = levels.easy(solution)
    print(solution2)
    gameui.show(puzzle,list(solution2))



if __name__ == "__main__":
    main()

