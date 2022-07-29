import random
import pygame
import sys

class Die:
    def __init__(self, sides):
        self.num_sides = sides
        self.face = None
        self.image = None
    
    def roll(self):
        self.face = random.randint(1, self.num_sides)

    def viz(self):
        if self.face != None:
            self.image = pygame.image.load(f"face{self.face}.png")
        return self.image

pygame.init()
window = pygame.display.set_mode((360, 360))
pygame.display.set_caption("Roll It!")

appFont = pygame.font.SysFont('ubuntu', 18)

die1 = Die(6)
die2 = Die(6)

die1.roll()
die2.roll()

def run():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rolling_sound = pygame.mixer.Sound(f"dice-{random.randint(1, 29)}.wav")
            rolling_sound.play()
            die1.roll()
            die2.roll()
    
    die1Text = appFont.render(f"{die1.face}", True, (0,0,0),(255,255,255))
    die1Rect = pygame.Rect(30, 30, 128, 128)

    die2Text = appFont.render(f"{die2.face}", True, (0,0,0),(255,255,255))
    die2Rect = pygame.Rect(170, 30, 128, 128)

    window.fill((0,128,0))

    # If the visual does not load properly, display the number as text
    # Otherwise, display the image of the die
    if die1.viz() is None:
        window.blit(die1Text, die1Rect)
    else:
        window.blit(die1.viz(), die1Rect)

    if die2.viz() is None:
        window.blit(die2Text, die2Rect)
    else:
        window.blit(die2.viz(), die2Rect)

    pygame.draw.rect(window, (0,0,0), die1Rect, width=1)
    pygame.draw.rect(window, (0,0,0), die2Rect, width=1)

    pygame.display.update()

while True:
    run()
