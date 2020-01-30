"""
The mother board of the operation.
30-01-2020 """

import cv2
import pyScripts.VideoData as RunVideo


class MOTHERBOARD:
    def __init__(self, video: RunVideo.VIDEO, numFramesCount: int, ballMovingThreshold: float, isdrawContours: bool):
        """
        Makes the main frame work that analyzes the video
        :param video:
        :param numFramesCount: int
        :param ballMovingThreshold: int
        :param isdrawContours: bool
        :return None
        """
        # Processing info
        self.video = video
        self.numFramesCount, self.ballMovingThreshold, self.isdrawContours \
            = numFramesCount, ballMovingThreshold, isdrawContours

        # Processing Data
        self.ballsMoving = False
        self.cutTimes = []

    def processVideo(self):
        """
        Processes the video and returns cutTimes
        All the information that relates to shot analysis sensitivity is in the parameters here
        :return: None
        """
        print('Processing Video...')
        while self.video.cap.isOpened():
            self.video.nextFrame()
            self.updateCutTimes()
            self.video.displayVideo()

            if cv2.waitKey(40) == 27:
                break

        self.video.closeVideo()

    def updateCutTimes(self):
        """
        looks at videoData and analyzes if the ball is moving or not
        It then updates the cut times list
        :return: None
        """
        self.video.checkFrameList(self.isdrawContours, self.numFramesCount)
        # Update Cut Times
        if self.video.frameData.isBallMoving(self.ballMovingThreshold) and not self.ballsMoving:
            self.ballsMoving = True
            self.cutTimes.append(self.video.frameNum)
            print(self.cutTimes)
        elif not self.video.frameData.isBallMoving(self.ballMovingThreshold) and self.ballsMoving:
            self.ballsMoving = False
            self.cutTimes.append(self.video.frameNum)
            print(self.cutTimes)







