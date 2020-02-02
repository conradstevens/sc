"""
The mother board of the operation.
30-01-2020 """

import cv2
import processingScripts.VideoData as RunVideo
import processingScripts.LoadBar as LoadBar
import editingScripts.CutTimesWriter as CutTimesWriter


class MOTHERBOARD:
    def __init__(self, video: RunVideo.VIDEO, numFramesCount: int, ballMovingThreshold: float,
                 isDrawContours: bool, playVideo):
        """
        Makes the main frame work that analyzes the video
        :param video:
        :param numFramesCount: int
        :param ballMovingThreshold: int
        :param isDrawContours: bool
        :return None
        """
        # Processing info
        self.video = video
        self.playVideo = playVideo
        self.numFramesCount, self.ballMovingThreshold, self.isDrawContours \
            = numFramesCount, ballMovingThreshold, isDrawContours

        # Processing Data
        self.ballsMoving = False
        self.cutTimes = []
        self.cutTimeWriter = CutTimesWriter.CUTTIMEWRITER()

    def processVideo(self):
        """
        Processes the video and returns cutTimes
        All the information that relates to shot analysis sensitivity is in the parameters here
        :return: None
        """
        loadingBar = LoadBar.LOADBAR('|--------------- Processing Video ---------------|', self.video)

        while self.video.cap.isOpened():
            self.video.nextFrame()
            if cv2.waitKey(40) == 27 or self.video.frameNum >= self.video.numFrames:
                break

            self.updateCutTimes()
            loadingBar.updateBar(self.video.frameNum)

            if self.playVideo:
                self.video.displayVideo()

        self.video.closeVideo()

    def updateCutTimes(self):
        """
        looks at videoData and analyzes if the ball is moving or not
        It then updates the cut times list
        :return: None
        """
        self.video.checkFrameList(self.isDrawContours, self.numFramesCount)
        # Update Cut Times
        if self.video.frameData.isBallMoving(self.ballMovingThreshold) and not self.ballsMoving:
            self.ballsMoving = True
            self.addCutTime()
        elif not self.video.frameData.isBallMoving(self.ballMovingThreshold) and self.ballsMoving:
            self.ballsMoving = False
            self.addCutTime()

    def addCutTime(self):
        """
        Adds cut time data to table and list
        :return: None
        """
        self.cutTimes.append(self.video.frameNum)
        self.cutTimeWriter.wrie(self.video.frameNum, self.ballsMoving)






