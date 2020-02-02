"""
Load bar showing how long it will take for the video to be finished processing
31-01-2020"""
import cv2
import numpy as np
from colr import color
import processingScripts.VideoData as VideoData


class LOADBAR:
    def __init__(self, barMessage, video: VideoData.VIDEO):
        """
        Prints a load bar in console
        """
        self.numFrames = video.numFrames
        self.frameCount = 0
        self.loadBarCount = 0  # Maxes out at maxBarLen
        self.maxLenBar = len(barMessage)
        print(barMessage)

    def updateBar(self, frameNum: int):
        """
        updates the loading bar
        :param frameNum: int
        :return:
        """
        numLoadBlocks = np.floor(frameNum/ self.numFrames * 50)
        while self.loadBarCount < numLoadBlocks:
            print(color('█', fore='green'), end='')
            self.loadBarCount += 1






