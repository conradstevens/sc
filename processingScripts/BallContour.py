"""
A single Contour of a moving object
29-01-2020 """
import numpy as np
import FindTable
from colr import color


class BALLCONTOUR:
    def __init__(self, x: int, y: int, w: int, h: int, frame):
        self.x, self.y, self.w, self.h, = x, y, w, h
        self.frameHeight, self.frameWidth, _ = frame.shape
        self.frame = frame

        self.pixelCount = 0
        self.colour = [0, 0, 0]

    def isBall(self) -> bool:
        """
        Returns the contour is surrounding a ball
        :return: bool
        """
        self.getContourColour()
        # print(color('██████    ' + str(self.colour) + '    ' + str(self.checkColourInRange()),
        #            fore=self.colour, back=(0, 0, 0)))
        if self.checkColourInRange():
            return self.checkColourInRange()

    def getContourColour(self) -> np.array:
        """
        returns the average colour found along the contour line
        :return: np.array
        """
        yCount = max(1, self.h % 4)
        xCount = max(1, self.w % 4)

        for yi in range(self.y, self.y + self.h, yCount):
            self.contoursSizeCheck(yi, self.x)
            self.contoursSizeCheck(yi, self.x + self.w)
        for xi in range(self.x, self.x + self.w, xCount):
            self.contoursSizeCheck(self.y, xi)
            self.contoursSizeCheck(self.y + self.h, xi)

        # Average Pixels
        self.colour = [self.colour[0] / self.pixelCount,
                       self.colour[1] / self.pixelCount,
                       self.colour[2] / self.pixelCount]

        return np.array(self.colour)

    def contoursSizeCheck(self, y, x):
        """
        If [y, x] is in the frame add it to the colour count
        :param y: int
        :param x: int
        :return: None
        """
        if y < self.frameHeight and x < self.frameWidth:
            pixelColour = self.frame[y, x]

            self.colour = [self.colour[0] + pixelColour[2],
                           self.colour[1] + pixelColour[1],
                           self.colour[2] + pixelColour[0]]
            self.pixelCount += 1

    def checkColourInRange(self) -> bool:
        """
        returns True iff the self.colour is in the colour range of the table
        :return: bool
        """
        # noinspection PyChainedComparisons
        return (FindTable.LOWCLOTH[0] < self.colour[0] and self.colour[0] < FindTable.HIGHCLOTH[0] and
                FindTable.LOWCLOTH[1] < self.colour[1] and self.colour[1] < FindTable.HIGHCLOTH[1] and
                FindTable.LOWCLOTH[2] < self.colour[2] and self.colour[2] < FindTable.HIGHCLOTH[2])
