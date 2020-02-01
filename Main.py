"""
Eddies videos people playing pool by fast-forwarding through parts where the balls aren't moving
Conrad Stevens
25/01/2020
"""
import processingScripts.VideoData as RunVideo
import processingScripts.ProcessVido as ProcessVideo
import editingScripts.VideoEditor as VideoEdditor


if __name__ == '__main__':
    video = RunVideo.VIDEO(vidName='MaxEveryVid.mp4', outputName='outputProcessVid')
    motherBoard = ProcessVideo.MOTHERBOARD(video, 12, 0.7, True)
    motherBoard.processVideo()
    videoEditor = VideoEdditor.VIDEOEDDITOR(videoName='MaxEveryVid.mp4', exportName='outputEditedVid.mp4', fps=video.fps)
    videoEditor.editVideo()


