"""
Keeps track of the most recent frames and determines what time is considered shot time
29-01-2020 """
import processingScripts.BallContour as BallContour

class FRAMELIST:
    def __init__(self):
        self.frameList = []
        self.shotTimes = []
        self.time = -1

    def popFrame(self, isBallMovement: bool, lenFrameList: int):
        """
        keeps the self.frameList up to date
        :param isBallMovement: bool
        :param lenFrameList: int
        :return: None
        """
        if len(self.frameList) > lenFrameList:
            self.frameList.pop(0)
        self.frameList.append(isBallMovement)

    def isBallMoving(self, percentOfFrames) -> bool:
        """
        Returns true if at least the percent of frames the 10 most recent frames have a moving ball in it
        :param percentOfFrames: float
        :return: bool
        """
        ballFrameCount = 0
        for i in self.frameList:
            if i:
                ballFrameCount += 1
        return ballFrameCount/len(self.frameList) > percentOfFrames




