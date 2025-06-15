import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(title='Astroid Shooter')

# create a surface
#test_surf = pygame.surface((400, 100))

while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updates
    #display_surface.blit(test_surf, (0, 0))
    
    # show the frame to player / update display surface
    pygame.display.update()