import pygame

pygame.init()

size = width, height = 1000, 600
speed = [2, 2]
bg = 22, 22, 22

screen = pygame.display.set_mode(size)

name = pygame.image.load("name.png")
namerect = name.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit()
    
    screen.fill(bg)
    screen.blit(name,namerect)
    pygame.display.flip()
