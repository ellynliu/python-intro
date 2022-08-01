import pygame
import sys

pygame.init()

# Make the mouse cursor disappear
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

window = pygame.display.set_mode((300, 300))
rect = pygame.Rect(0, 0, 0, 0)
rect.center = window.get_rect().center

# Create a list to store the pacman images
imgs = []
for i in range(6):
    imgs.append(pygame.image.load(f"pacman/pacman{i}.png"))

num_imgs = len(imgs)
img_idx = 0
frame_rate = 10 # per second
frame_mills = 1000 / frame_rate # number of milliseconds per frame

def run():
    global img_idx

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rect.x = mouse_x
    rect.y = mouse_y

    # update image
    if pygame.time.get_ticks() % frame_mills == 0:
        img_idx += 1

    window.fill(0)
    window.blit(imgs[img_idx % num_imgs], rect)

    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.update()

while True:
    run()
