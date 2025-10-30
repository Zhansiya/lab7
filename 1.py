import pygame
import math
import datetime
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

background = pygame.image.load("background.png").convert_alpha()
background = pygame.transform.smoothscale(background, (500, 500))

right_hand = pygame.image.load("right.png").convert()
right_hand.set_colorkey((255, 255, 255))

left_hand = pygame.image.load("left.png").convert()
left_hand.set_colorkey((255, 255, 255))


center = (250, 250)

def blit_rotate(surf, image, pos, originPos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    second = now.second
    minute = now.minute

    second_angle = -6 * second
    minute_angle = -6 * (minute + second / 60)

    screen.blit(background, (0, 0))
    blit_rotate(screen, right_hand, center, (0, 0), minute_angle)
    blit_rotate(screen, left_hand, center, (0, 0), second_angle)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
