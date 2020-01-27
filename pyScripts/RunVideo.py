"""
 Runs the video and documents the times
 25/01/2020"""

import cv2
import os
import pyScripts.FindMovement as FindMovement
import FindTable


class VIDEO:
    def __init__(self, vidName: str, tableName: str, outputName: str):
        """
        Processes the video and produces output
        :param vidName: str
        :param outputName: str
        """
        self.cap = cv2.VideoCapture(getVidAddress(vidName))
        ret, self.frame1 = self.cap.read()
        ret, self.frame2 = self.cap.read()

        # Processing Classes
        self.movement = FindMovement.MOVEMENT(self.frame1, self.frame2)
        # self.table = FindTable.TABLE(tableName)

        # Make Output
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.out = cv2.VideoWriter(getOuputAddress(outputName), fourcc, 5.0, (1280, 720))

    def process(self):
        """
        Processes the video and saves an analyzed version in the output folder
        :return: None
        """
        while self.cap.isOpened():

            self.nextFrame()
            self.getContours(True)
            self.displayVideo()

            # Allow Escape
            if cv2.waitKey(40) == 27:
                break

        self.closeVideo()

    def nextFrame(self):
        """
        moves the video allong to the next frame
        :return: None
        """
        self.frame1 = self.frame2
        ret, self.frame2 = self.cap.read()

    def displayVideo(self):
        """
        Displays the live video on the screen and saves a copy of the video in the folder as output
        :return: None
        """
        image = cv2.resize(self.frame1, (1280, 720))
        self.out.write(image)
        cv2.imshow("PoolVideo", self.frame1)

    def getContours(self, drawContours: bool):
        """
        Gets all the contour lines of moving objects
        :param drawContours:
        :return: None
        """
        self.movement.getContours(self.frame1, self.frame2)
        if drawContours:
            for contour in self.movement.contours:
                self.drawContours(contour, 1000)

    def drawContours(self, contour, maxBallSize):
        """
        Draws the contours of the lines live
        :param contour: list of all contour objects
        :param maxBallSize: the largest contour size to be drawn
        :return: None
        """
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < maxBallSize:
            cv2.rectangle(self.frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(self.frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 3)

    def closeVideo(self):
        """
        Closes the video and stops the run video script
        :return: None
        """
        cv2.destroyAllWindows()
        self.cap.release()
        self.out.release()


def getVidAddress(vidName: str):
    """
    Returns the address of the video being processed
    :param vidName: str
    :return: None
    """
    thisPath = os.path.dirname(os.path.realpath(__file__))
    return thisPath + '\\videos\\' + vidName


def getOuputAddress(outVidName: str):
    """
    Returns the address of the location where the processed video will be saved
    :param outVidName: str
    :return:None
    """
    thisPath = os.path.dirname(os.path.realpath(__file__))
    return thisPath + '\\output\\' + outVidName + '.avi'
