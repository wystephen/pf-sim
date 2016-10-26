# -*- coding:utf-8 -*-
# carete by steve at  2016 / 10 / 26　17:10


import pygame


class BeaconWithRange:
    '''

    '''

    def __init__(self,SCREEN_SIZE,OFFSET,ScaleFactor=1.0):
        '''

        :param SCREEN_SIZE:
        :param OFFSET: piexels
        :param ScaleFactor: Real(m) to piexels
        '''

        self.SCREEN_SIZE = SCREEN_SIZE
        self.OFFSET = OFFSET
        self.SCALEFACTOR = ScaleFactor

        self.Pose = [10,10]
        self.Dist  = 0

        self.IntPose = [1,1]
        self.IntDist = 0

    def SetPose(self,x,y):
        self.Pose = [x,y]
        for i in range(len(self.Pose)):
            self.IntPose[i] = int(self.Pose[i]*1.0/self.SCALEFACTOR) + self.OFFSET[i]


    def SetRange(self,distance):
        self.Dist = distance
        self.IntDist = int(distance * 1.0 / self.SCALEFACTOR)

    def Draw(self,screen):
        pygame.draw.circle(screen,
                           [0,22,211],
                           self.IntPose,
                           self.IntDist,1)

    def ComputeRange(self,the_pose):
        tmp_distance = 0.0
        for i in range(len(self.Pose)):
            tmp_distance += (self.Pose[i]*1.0 - the_pose[i]*1.0) ** 2.0
        tmp_distance = tmp_distance ** 0.5

        self.SetRange(tmp_distance)






