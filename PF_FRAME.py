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
        #Methond 1
        # dis_err = 0
        # for i in range((self.BeaconSet.shape[1])):
        #     dis_err += (np.linalg.norm(self.BeaconSet[i,:] - pose) - Ranges[i]) ** 2.0
        #
        # return 1/dis_err ** 0.5
        #Methond 2
        dis = 0.0
        score = 0.0
        for i in range(self.BeaconSet.shape[0]):
            dis = np.linalg.norm(self.BeaconSet[i,:]-pose)
            score *= self.NormPdf(Ranges[i],dis,12.0)
        return score


    def NormPdf(self,x,miu,sigma):
        para1 = 1/ np.sqrt(2.0 * np.pi) / sigma
        para2 = - (x-miu) ** 2.0 / sigma/sigma
        return para1 * np.exp(para2)

    def ReSample(self):
        self.Wight /= self.Wight.sum()
        self.Beta = self.Wight

        # tmp_Wight = self.Wight
        tmp_P_state = self.P_state

        for i in range(self.P_state.shape[0]):
            if i >0:
                self.Beta[i] = self.Beta[i-1] + self.Wight[i]

        for i in range(self.P_state.shape[0]):
            tmp_rnd = np.random.uniform(0.0, 1.0)

            for j in range(self.P_state.shape[0]):
                if tmp_rnd < self.Beta[j]:
                    tmp_P_state[i,:] = self.P_state[j,:]
                    # print("j:",j)
                    break

                # if j > 999:
                #     print("j:",j)

                # print(j)

        # self.Wight = np.ones_like(self.Wight)
        # self.Wight /= self.Wight.sum()

        self.P_state = tmp_P_state


    def Draw(self,screen):

        for k in range(self.P_state.shape[0]):
            IntPose = [0,0]
            for i in range(self.P_state.shape[1]):
                IntPose[i] = int(self.P_state[k,i] / self.SCALEFACTOR) + self.OFFSET[i]
            pygame.draw.circle(screen,[200,200,2],IntPose,int(self.Wight[k]/self.Wight.max()),int(self.Wight[k]/self.Wight.max()))
            # print(k)


