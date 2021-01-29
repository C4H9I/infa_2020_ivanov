import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

color = (255, 255, 255)
yellow_color = 'yellow'
black_color = 'black'
red_color = 'red'

center = (200,200)
radius = 50

#main circle
circle(screen, yellow_color, center, radius)

#ayes 
circle(screen, red_color, (185,185), radius/3.5)
circle(screen, black_color, (185,185), radius/6)

circle(screen, red_color, (215,185), radius/4)
circle(screen, black_color, (215,185), radius/7)

#left brow
left_brow_start_pos = (145, 150)
left_brow_end_pos = (190, 160)
width = 5
line(screen, red_color, left_brow_start_pos, left_brow_end_pos, width)

#left brow
rt_brow_start_pos = (210, 160)
rt_brow_end_pos = (235, 150)
width = 5
line(screen, red_color, rt_brow_start_pos, rt_brow_end_pos, width)

#mouth
line(screen, black_color, (175,225), (225,225), 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
