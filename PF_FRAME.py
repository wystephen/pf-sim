# -*- coding:utf-8 -*-
# carete by steve at  2016 / 10 / 27　9:17

import pygame

import numpy as np
import scipy as sp

class PF_Frame:
    def __init__(self,SCREEN_SIZE,OFFSET,ScaleFactor,Particle_num):
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

        self.P_state = np.zeros([Particle_num,2])
        self.Wight = np.ones(Particle_num)

        self.EstimatePose = self.Pose

        self.BeaconSet = np.zeros([3,2])

    def SetBeaconSet(self,beaconset):
        self.BeaconSet = beaconset

    def InitialPose(self,pose):
        for i in range(len(pose)):

            self.Pose[i] = float(pose[i])\
                           * 1.0 *\
                           self.SCALEFACTOR

            self.IntPose[i] = int(self.Pose[i] * 1.0 / self.SCALEFACTOR) + self.OFFSET[i]

        for k in range(self.P_state.shape[0]):
            self.P_state[k,:] = self.Pose
        self.Sample(1.1)


    def Sample(self,sigma):
        rand_pose_offset = np.random.normal(0.0,sigma,self.P_state.shape)

        self.P_state += rand_pose_offset

    def Evaluated(self,Ranges):
        for k in range(self.P_state.shape[1]):
            self.Wight[k] = self.Score(Ranges,self.P_state[k,:])


    def Score(self,Ranges,pose):
        dis_err = 0
        for i in range(len(self.BeaconSet.shape[1])):
            dis_err += np.linalg.norm(self.BeaconSet[i,:] - pose) - Ranges[i]

        return dis_err ** 0.5

    def ReSample(self):
        


    def Draw(self,screen):

        for k in range(self.P_state.shape[0]):
            IntPose = [0,0]
            for i in range(self.P_state.shape[1]):
                IntPose[i] = int(self.P_state[k,i] / self.SCALEFACTOR) + self.OFFSET[i]
            pygame.draw.circle(screen,[200,200,2],IntPose,int(self.Wight[k]/self.Wight.max()),int(self.Wight[k]/self.Wight.max()))


