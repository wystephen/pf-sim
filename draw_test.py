# -*- coding:utf-8 -*-
# carete by steve at  2016 / 10 / 26　16:50


import pygame

from Beacon import BeaconWithRange

if __name__ == '__main__':
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

    tmp_beacon = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)
    tmp_beacon2 = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)
    tmp_beacon3 = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)

    tmp_beacon.SetPose(100,100)
    tmp_beacon2.SetPose(1000,500)

    tmp_beacon3.SetPose(1300,200)



    while not done:
        pose = pygame.mouse.get_pos()

        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                print(event.key)


        screen.fill(BLACK)
        pygame.draw.circle(screen,[110,10,155],pose,20,3)


        tmp_beacon.ComputeRange(pose)
        tmp_beacon2.ComputeRange(pose)

        tmp_beacon3.ComputeRange(pose)

        # tmp_beacon.SetRange(pose[1]+2)
        tmp_beacon.Draw(screen)
        tmp_beacon2.Draw(screen)
        tmp_beacon3.Draw(screen)



        pygame.display.flip()

        # clock.tick(5)

    pygame.quit()


