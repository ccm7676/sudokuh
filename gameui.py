import pygame
pygame.init()
size = width, height = 1000, 600
bg = 22,22,22

screen = pygame.display.set_mode(size)
font = pygame.font.Font('Montserrat-Bold.ttf', 35)

board = pygame.image.load("board.png")
boardrect = board.get_rect()

horizontal = pygame.image.load("horizontal.png")
horizontalrect = horizontal.get_rect()

vertical = pygame.image.load("vertical.png")
verticalrect = vertical.get_rect()

verticalrect.x = 55
verticalrect.y = 75

horizontalrect.x = 55
horizontalrect.y = 75

boardrect.x = 50
boardrect.y = 70

texts = []
textrects = []

selected_x = 0
selected_y = 0


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

def set_lines(distance_x,distance_y):
    global selected_x
    global selected_y

    if distance_x < 50:
        verticalrect.x = 55
        selected_x = 0
    elif distance_x < 100:
        verticalrect.x = 105
        selected_x = 1
    elif distance_x < 150:
        verticalrect.x = 155 
        selected_x = 2
    elif distance_x < 200:
        verticalrect.x = 207
        selected_x = 3
    elif distance_x < 250:
        verticalrect.x = 257 
        selected_x = 4
    elif distance_x < 300:
        verticalrect.x = 307
        selected_x = 5
    elif distance_x < 350:
        verticalrect.x = 360
        selected_x = 6
    elif distance_x < 400:
        verticalrect.x = 410
        selected_x = 7
    elif distance_x < 450:
        verticalrect.x = 460
        selected_x = 8

    if distance_y < 50:
        horizontalrect.y = 75
        selected_y = 0
    elif distance_y < 100:
        horizontalrect.y = 125
        selected_y = 1
    elif distance_y < 150:
        horizontalrect.y = 175      
        selected_y = 2
    elif distance_y < 200:
        horizontalrect.y = 228
        selected_y = 3
    elif distance_y < 250:
        horizontalrect.y = 280   
        selected_y = 4
    elif distance_y < 300:
        horizontalrect.y = 330
        selected_y = 5
    elif distance_y < 350:
        horizontalrect.y = 383
        selected_y = 6
    elif distance_y < 400:
        horizontalrect.y = 433
        selected_y = 7
    elif distance_y < 450:
        horizontalrect.y = 483     
        selected_y = 8



def text_blit():
    for i in range(len(texts)):
        screen.blit(texts[i],textrects[i])



def show(puzzle, solution):
    original = puzzle
    puzzle = puzzle
    
    while True:
        display_puzzle(puzzle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
        
        mouse_pressed = pygame.mouse.get_pressed()[0]

        distance_x = pygame.mouse.get_pos()[0] - 55;
        distance_y = pygame.mouse.get_pos()[1] - 75;
        
        if mouse_pressed == True:
           set_lines(distance_x,distance_y)

        keys_down = pygame.key.get_pressed()

        if puzzle[selected_x][selected_y] == -1 or puzzle[selected_y][selected_x] != original[selected_y][selected_x]:
        
            if keys_down[pygame.K_1]:
                puzzle[selected_y][selected_x] =1
            elif keys_down[pygame.K_2]:
                puzzle[selected_y][selected_x] =2
            elif keys_down[pygame.K_3]:
                puzzle[selected_y][selected_x] =3
            elif keys_down[pygame.K_4]:
                puzzle[selected_y][selected_x] =4
            elif keys_down[pygame.K_5]:
                puzzle[selected_y][selected_x] =5
            elif keys_down[pygame.K_6]:
                puzzle[selected_y][selected_x] =6
            elif keys_down[pygame.K_7]:
                puzzle[selected_y][selected_x] =7
            elif keys_down[pygame.K_8]:
                puzzle[selected_y][selected_x] =8
            elif keys_down[pygame.K_9]:
                puzzle[selected_y][selected_x] =9
        screen.fill(bg)
        screen.blit(board, boardrect)
        screen.blit(vertical,verticalrect)
        screen.blit(horizontal,horizontalrect)
        text_blit()
        pygame.display.flip()

