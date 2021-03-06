"""
Finds the movement of the balls
25/01/2020 """
import cv2
import processingScripts.BallContour as BallContour
import FindTable


class MOVEMENT:
    def __init__(self, frame1, frame2, minBallSize, maxBallSize, videoSensitivity):
        """
        Analyzes frame 1 and 2 to determine if there is motion
        :param frame1: frame
        :param frame2: frame
        """
        self.frame1 = frame1; self.frame2 = frame2
        self.minBallSize, self.maxBallSize = minBallSize, maxBallSize
        self.videoSensitivity = videoSensitivity

        self.contours = []
        self.frameHeight, self.frameWidth, _ = self.frame1.shape
        self.balls = []

    def getContours(self, frame1, frame2) -> list:
        """
        :return: list of contour lines
        :param frame1: frame
        :param frame2: frame
        :return:
        """
        self.frame1 = frame1; self.frame2 = frame2

        # Find Moving Objects
        diff = cv2.absdiff(self.frame1, self.frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=self.videoSensitivity)  # Sensitivity
        self.contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.updateBalls()
        return self.contours

    def updateBalls(self):
        """
        Updates the list of balls on the table
        Makes sure it is of the rite size and the contour is of the right colour
        :return: None
        """
        self.balls = []
        for contour in self.contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            # Checks size
            if (self.minBallSize < w < self.maxBallSize and
                    self.minBallSize < h < self.maxBallSize):
                ballContour = BallContour.BALLCONTOUR(x, y, w, h, self.frame1)

                # Checks Colour
                if ballContour.isBall():
                    self.balls.append(ballContour)
