"""
Eddies videos people playing pool by fast-forwarding through parts where the balls aren't moving
Conrad Stevens
25/01/2020
"""
import processingScripts.VideoData as RunVideo
import processingScripts.ProcessVido as ProcessVideo


if __name__ == '__main__':
    video = RunVideo.VIDEO(vidName='poolVid.mp4', outputName='outputProcessVid')
    motherBoard = ProcessVideo.MOTHERBOARD(video, 12, 0.7, True)
    motherBoard.processVideo()


