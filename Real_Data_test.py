# -*- coding:utf-8 -*-
# Create by steve in 16-10-28 at 上午8:56

import pygame

import numpy as np

from Beacon import BeaconWithRange

from Agent import Robo

from PF_FRAME import PF_Frame

if __name__ == '__main__':
    # --- Clobals ---
    # Colors

    BLACK=(0,0,0)
    WHITE=(255,255,255)

    SCREEN_SIZE=[1680,980]

    OFFSET = [300,300] # piexels

    ScaleFactor = 80.0 #Real(m) to piexels


    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.display.set_caption("Real Test.")

    allspriteslit = pygame.sprite.Group()

    clock = pygame.time.Clock()
    done = False

    tmp_beacon = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)
    tmp_beacon2 = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)
    tmp_beacon3 = BeaconWithRange(SCREEN_SIZE,OFFSET,ScaleFactor)

    beaconpose = np.loadtxt("beacon_set.csv",delimiter=",")
    print(beaconpose)
    tmp_beacon.SetPose(beaconpose[0,0],beaconpose[0,1])
    tmp_beacon2.SetPose(beaconpose[1,0],beaconpose[1,1])
    tmp_beacon3.SetPose(beaconpose[2,0],beaconpose[2,1])

    # Data Load
    beacon_range = np.loadtxt("beacon_out.txt")
    gt = np.loadtxt("gt.csv",delimiter=",")


    time_step = 0
    # Data preprocess 1:3d to 2d
    z_offset = beaconpose[:,2] - 1.12
    z_offset = z_offset

    z_offset.reshape([1,3])
    beacon_range = beacon_range[:,3:6]
    beacon_range = beacon_range**2.0 - z_offset **2.0
    beacon_range = beacon_range ** 0.5

    print("bea range",beacon_range)

    # Data preprocess 2:gt cut
    gt = gt[:,0:2]

    tmp_beacon.SetRangeMethond(1)
    tmp_beacon2.SetRangeMethond(1)
    tmp_beacon3.SetRangeMethond(1)

    tmp_robo = Robo(SCREEN_SIZE,OFFSET,ScaleFactor)

    pf = PF_Frame(SCREEN_SIZE,OFFSET,ScaleFactor,1300)

    BeaconSet = np.zeros([3,2])

    BeaconSet[0,:] = tmp_beacon.Pose
    BeaconSet[1,:] = tmp_beacon2.Pose
    BeaconSet[2,:] = tmp_beacon3.Pose

    pf.SetBeaconSet(BeaconSet)

    pygame.mouse.set_visible(False)

    last_pose = np.zeros(2)

    while not done:
        pose = pygame.mouse.get_pos()
        # print("dis:",np.linalg.norm(np.asarray(pose)-last_pose))
        last_pose = np.asarray(pose)

        if time_step == 0:
            pf.InitialPose(gt[0,:])

        time_step += 1
        if time_step == beacon_range.shape[0]-1:
            time_step = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 115:
                    pf.InitialPose([((pose[0]-OFFSET[0])*1.0/ScaleFactor),((pose[1]-OFFSET[1])*1.0/ScaleFactor)])
                    # print("test pose:",[((pose[0]-OFFSET[0])*1.0/ScaleFactor),((pose[1]-OFFSET[1])*1.0/ScaleFactor)])



        screen.fill(BLACK)
        # pygame.draw.circle(screen,[110,10,155],pose,20,3)

        # tmp_pose = np.asarray(pose)
        # for i in range(len(pose)):
        #     tmp_pose[i] = (pose[i] - OFFSET[i])/ScaleFactor
        # pose = tmp_pose
        # tmp_beacon.ComputeRange(pose)
        # tmp_beacon2.ComputeRange(pose)
        # tmp_beacon3.ComputeRange(pose)
        print(time_step)

        tmp_beacon.SetRange(beacon_range[time_step,0])
        tmp_beacon2.SetRange(beacon_range[time_step,1])
        tmp_beacon3.SetRange(beacon_range[time_step,2])

        # tmp_beacon.SetRange(pose[1]+2)
        tmp_beacon.Draw(screen)
        tmp_beacon2.Draw(screen)
        tmp_beacon3.Draw(screen)

        #Robot draw
        # tmp_robo.SetPose(pose)
        tmp_robo.SetPose(gt[time_step,:])
        tmp_robo.Draw(screen)
        print(gt[time_step,:])


        pf.Sample(0.2)
        # print("real range:" ,[tmp_beacon.GetRange(pose,0.1),
        #               tmp_beacon2.GetRange(pose,0.1),
        #               tmp_beacon3.GetRange(pose,0.1)])

        # pf.Evaluated([tmp_beacon.GetRange([((pose[0]-OFFSET[0])*1.0/ScaleFactor),((pose[1]-OFFSET[1])*1.0/ScaleFactor)],0.1)*1.0,
        #               tmp_beacon2.GetRange([((pose[0]-OFFSET[0])*1.0/ScaleFactor),((pose[1]-OFFSET[1])*1.0/ScaleFactor)],0.1)*1.0,
        #               tmp_beacon3.GetRange([((pose[0]-OFFSET[0])*1.0/ScaleFactor),((pose[1]-OFFSET[1])*1.0/ScaleFactor)],0.1)*1.0])

        pf.Evaluated(beacon_range[time_step,:])

        pf.ReSample()
        pf.Draw(screen)

        # pygame.draw.rect(screen,[0,100,100],[pose[0],pose[1],10,10],10)

        pygame.display.flip()

        # clock.tick(1)

    pygame.quit()

'''
kkk,ikomtg inum,onkkkkkkuiiiiiiiiiiiibu[[i.n m iooojjjknmunumkkkkkkllllkkkdd
'''

