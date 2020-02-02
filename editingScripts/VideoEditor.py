"""
Edits the video to fast-forwards through parts where isBallMoving is false
31-01-2020 """

import os
import pandas as pd
import numpy as np
import moviepy.editor as mpEditor
import moviepy.Clip as mpClip
from moviepy.video.fx import accel_decel
import processingScripts.VideoData as VideoData


class VIDEOEDDITOR:
    def __init__(self, videoName: str, exportName: str, fps: int):
        """
        Object that does editing
        :param videoName: str
        :param exportName: str
        :param fps: int
        """
        # Basic data
        print('Loading Editing Data...')
        self.cutData = pd.read_csv(
                                    os.path.dirname(os.path.realpath(__file__)) + '\\CutTimesTable.txt',
                                    delimiter=';',
                                    names=['frameNum', 'isBallMoving'])
        self.fps = fps
        self.lastFrame = -1
        self.thisFrame = 0
        self.exportName = exportName

        # Editing Objects
        print('Loading Video...')
        self.originalVideo = mpEditor.VideoFileClip(VideoData.getVidAddress(videoName))
        self.clipList = []

    def editVideo(self):
        """
        Reads the CutTimesTable and edits the video accordingly
        Saves a copy of the edited video to outputs
        :return: None
        """
        print('Editing Video...')
        self.makeClipList()
        outPut = mpEditor.CompositeVideoClip(self.clipList)
        outPut.write_videofile(self.exportName, codec='libx264')

    def makeClipList(self):
        """
        Generates all the clips that will be concatenated to generate the video
        :return: None
        """

        for t in self.cutData.itertuples():
            self.lastFrame = self.thisFrame
            self.thisFrame = t.frameNum
            self.clipList.append(self.cutVideo(self.lastFrame, self.thisFrame, t.isBallMoving))

    def cutVideo(self, frame1: int, frame2: int, isFastForwards: bool) -> mpClip.Clip:
        """
        Splices the video then adds the clip to
        :param frame1: int
        :param frame2: int
        :param isFastForwards: bool
        :return: mpClip.Clip
        """
        clip = mpClip.Clip.subclip(self.originalVideo, self.fps2Sec(frame1), self.fps2Sec(frame2))
        if isFastForwards:
            newTime = 0.5*(frame2 - frame1)  # double speed
            clip = accel_decel.accel_decel(clip, newTime, 1, 1)

        return clip

    def fps2Sec(self, frameNum: int):
        """
        Returns the number of seconds that passed to reach that frame
        :param frameNum: int
        :return: int
        """
        return np.floor(frameNum / self.fps)

