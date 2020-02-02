"""
Used to determine an accurate colour range for the table
25/01/2020 """

import cv2
import numpy as np
import os

#############################################################################
#############################   Colour of Cloth #############################

LOWCLOTH = [0, 50, 140];                        HIGHCLOTH = [140, 240, 255]

#############################################################################
#############################################################################


class TABLE:
    def __init__(self, tableName: str, lowerCloth: list, upperCloth: list):
        """
        Gets information about the pool table in the frame
        :param tableName: str file name
        :param lowerCloth: list RGB
        :param upperCloth: list RGB
        """
        self.img = cv2.imread(getTableAddress(tableName))
        self.lowerCloth, self.upperCloth = np.array(lowerCloth), np.array(upperCloth)
        self.mask, self.res = -1, -1

    def processImage(self):
        """
        Creates self.mask and self.res
        :return: None
        """
        self.img = cv2.medianBlur(self.img, 15)
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(hsv, self.lowerCloth, self.upperCloth)
        self.res = cv2.bitwise_and(self.img, self.img, mask=self.mask)

    def displayImmage(self):
        """
        Shows all the images that aren't commented out
        :return:
        """
        # cv2.imshow('frame', self.img) # Shows the original image
        # cv2.imshow('mask', mask)      # Shows the area selected
        cv2.imshow('res', self.res)  # Shows all that is in the colour range
        cv2.waitKey(0)


def getTableAddress(tableName: str) -> str:
    """
    gets the adress of the table name
    :param tableName:
    :return: str
    """
    thisPath = os.path.dirname(os.path.realpath(__file__))
    return thisPath + '\\videos\\' + tableName


if __name__ == '__main__':
    """
    For testing out which colour interval works best
    """
    table = TABLE('poolTalbe.jpg', [30, 120, 150], [230, 230, 255])
    table.processImage()
    table.displayImmage()

