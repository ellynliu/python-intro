import pygame
import sys

pygame.init()

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
window = pygame.display.set_mode((600, 600))
rect = pygame.Rect(0, 0, 20, 20)

def run():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    rect.x = mouse_x
    rect.y = mouse_y

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.update()
    
while True:
    run()
