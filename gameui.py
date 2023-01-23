import pygame
pygame.init()
size = width, height = 1000, 600
bg = 22,22,22

screen = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 32)

board = pygame.image.load("board.png")
boardrect = board.get_rect()

boardrect.x = 50
boardrect.y = 70

texts = []
textrects = []

def display_puzzle(puzzle):
    offset_y = 100
    offset_x = 80

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != -1:
                texts.append(font.render(str(puzzle[i][j]), True, (255,255,255)))
            else:
                texts.append(font.render(" ", True, (255,255,255)))

            textrects.append(texts[len(texts)-1].get_rect())
            textrects[len(textrects) -1].center = (offset_x + 50*j,offset_y + 50*i)
        offset_y += 1.6

def text_blit():
    for i in range(len(texts)):
        screen.blit(texts[i],textrects[i])




def show(puzzle, solution):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()

        display_puzzle(puzzle)

        screen.fill(bg)
        screen.blit(board, boardrect)
        text_blit()
        pygame.display.flip()

