"""
Eddies videos people playing pool by fast-forwarding through parts where the balls aren't moving
Conrad Stevens
25/01/2020
"""
import pyScripts.RunVideo as RunVideo


def main(videoName:str, tableName: str, outputName:str):
    print("Processing Video...")
    video = RunVideo.VIDEO(videoName, tableName, outputName)
    video.process()


if __name__ == '__main__':
    main(videoName='poolVid.mp4', tableName='poolTalbe.jpg', outputName='outputVid')


