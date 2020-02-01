"""
Writes to the cut time writer
31-01-2020 """

import os


class CUTTIMEWRITER:
    def __init__(self):
        # self.cutWriter = open((os.path.dirname(os.path.realpath(__file__)) + '\\CutTimesTable'), "a")
        self.cutWriter = -1

    def wrie(self, frame: int, isBallMoving: bool):
        """
        Writes to the table
        :param frame: int
        :param isBallMoving: bool
        :return: None
        """
        self.cutWriter = open((os.path.dirname(os.path.realpath(__file__)) + '\\CutTimesTable.csv'), "a")
        self.cutWriter.write(str(frame) + ';' + str(isBallMoving) + '\n')
        self.cutWriter.close()




