import pygame
def button(screen, msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    text = smallText.render(msg, True, (255, 255, 255))
    Rect = text.get_rect()
    Rect.center = ((x + (w / 2)), (y + h / 2))
    screen.blit(text, Rect)
    myvalue = None
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(screen,ac,(x,y,w,h))
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        text = smallText.render(msg, True, (255, 255, 255))
        Rect = text.get_rect()
        Rect.center = ((x + (w / 2)), (y + h / 2))
        screen.blit(text, Rect)
        if click[0] == 1 and action != None and myvalue == None:
            myvalue = 1
            action()
            return False
        else:
            return True
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        text = smallText.render(msg, True, (255, 255, 255))
        Rect = text.get_rect()
        Rect.center = ((x + (w / 2)), (y + h / 2))
        screen.blit(text, Rect)
        return True

