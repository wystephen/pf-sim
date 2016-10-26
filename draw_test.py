# -*- coding:utf-8 -*-
# carete by steve at  2016 / 10 / 26　16:50


import pygame

# --- Clobals ---
# Colors

BLACK=(0,0,0)
WHITE=(255,255,255)

SCREEN_SIZE=[1680,980]

OFFSET = [10,10] # piexels

ScaleFactor = 1.0 #Real(m) to piexels


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Test All")

allspriteslit = pygame.sprite.Group()

clock = pygame.time.Clock()
done = False

while not done:
    pose = pygame.mouse.get_pos()

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            print(event.key)



    screen.fill(BLACK)
    pygame.draw.circle(screen,[0,10,155],pose,20,3)


    pygame.display.flip()

    # clock.tick(5)

pygame.quit()


