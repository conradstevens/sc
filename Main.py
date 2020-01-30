"""
Eddies videos people playing pool by fast-forwarding through parts where the balls aren't moving
Conrad Stevens
25/01/2020
"""
import pyScripts.VideoData as RunVideo
import pyScripts.ProcessVido as ProcessVideo


if __name__ == '__main__':
    print('----- Staring Analysis -----')
    video = RunVideo.VIDEO(vidName='poolVid.mp4', outputName='outputVid')
    motherBoard = ProcessVideo.MOTHERBOARD(video, 12, 0.7, True)
    motherBoard.processVideo()


