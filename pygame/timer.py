import pygame
import sys

# This program will run for five seconds, then automatically end.
# Logic: subtract time elapsed from five seconds to see how much time is left. 
# End program when time left is 0. 

pygame.init()
win = pygame.display.set_mode((300,300))
pygame.display.set_caption('Timer')

theFont = pygame.font.SysFont(False, 30)

totTime = 5 * 1000 # number of milliseconds in five seconds
timeLeft = totTime
t0 = pygame.time.get_ticks() # starting timestamp

def run():
    # update countdown
    timeElapsed = pygame.time.get_ticks() - t0
    timeLeft = totTime - timeElapsed

    timerText = theFont.render(f"{timeLeft}", True, (0,0,0), (255,255,255))
    timerRect = pygame.Rect(50, 80, 0, 0)

    win.blit(timerText, timerRect)

    pygame.draw.rect(win, (255,255,255), timerRect)

    pygame.display.update()

    if timeLeft <= 0:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    run()
