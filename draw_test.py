# -*- coding:utf-8 -*-
# carete by steve at  2016 / 10 / 26　16:50


import pygame

# --- Clobals ---
# Colors

BLACK=(0,0,0)
WHITE=(255,255,255)


pygame.init()

screen = pygame.display.set_mode([1080,920])

pygame.display.set_caption("Test All")

allspriteslit = pygame.sprite.Group()

clock = pygame.time.Clock()
done = False

while not done:
    pose = pygame.mouse.get_pos()

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.circle(screen,[0,10,155],pose,20,3)


    pygame.display.flip()

    # clock.tick(5)

pygame.quit()


