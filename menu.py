import pygame
import gameui

pygame.init()

size = width, height = 1000, 600
bg = 22, 22, 22

screen = pygame.display.set_mode(size)


name = pygame.image.load("name.png")
namerect = name.get_rect()

playbtn = pygame.image.load("playbtn.png")
playbtnrect = playbtn.get_rect()

settingsbtn = pygame.image.load("settingsbtn.png")
settingsbtnrect = settingsbtn.get_rect()


namerect.x = 178
namerect.y = 75

playbtnrect.x = 384
playbtnrect.y = 275

settingsbtnrect.x = 384
settingsbtnrect.y = 400



def show():
    while  True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0] and playbtnrect.collidepoint(pygame.mouse.get_pos()):
            return "play"
        
        screen.fill(bg)
        screen.blit(name,namerect)
        screen.blit(playbtn, playbtnrect)
        screen.blit(settingsbtn, settingsbtnrect)
        pygame.display.flip()


