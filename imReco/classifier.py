import cv2 as cv
import numpy as np


IMHEIGHT = 480

"""
This Classifier tries to find usable paths in the captured image. It is used
to tell the robot, where it is allowed to move.
It uses the Hough Line Transformation to detect lines in the images.

"""

class Classifier:
    def __init__(self):
        self.frame = None
        self.lines = None
        self.vlines = None  # vertical lines
        self.hlines = None  # horizontal lines

    def findLines(self):
        grayImg = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(grayImg, 50, 150, apertureSize=3)
        self.lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=200)

    def _sortLines(self):
        self.vlines = []
        self.hlines = []
        for line in self.lines.tolist():
            x1, y1, x2, y2 = line[0]
            if abs(x2 - x1) < abs(y2 - y1):
                self.vlines.append(line[0])
            else:
                self.hlines.append(line[0])

    """
    Detects branches.
    0 - left
    1 - forward
    2 - right
    3 - end
    """

    def detectBranches(self) -> list:
        branches = []

        if len(self.hlines) == 0:
            self.vlines.sort(key=lambda x: x[3], reverse=True)
            if self.vlines[0][3] < IMHEIGHT / 2:
                return [3]
            return [1]

        if len(self.vlines) == 0:
            print("no vlines found")
            return 1

        self.vlines.sort(key=lambda x: x[0])
        self.hlines.sort(key=lambda x: x[0])

        if self.hlines[0][0] < self.vlines[0][0]:  # check if left branch exists
            branches.append(0)

        if self.vlines[-1:][0][3] < self.hlines[-1:][0][3]:  # check if right branch exists
            branches.append(2)

        self.vlines.sort(key=lambda x: x[3], reverse=True)
        self.hlines.sort(key=lambda x: x[3], reverse=True)

        if self.hlines[0][3] < self.vlines[0][3]:  # check if path continues forward
            branches.append(1)

        return branches

    def classify(self, image: object = None) -> int:
        if image is not None:
            self.frame = image

        lines = self.findLines()
        f = self.frame
        if self.lines is not None:
            for line in self.lines:
                x1, y1, x2, y2 = line[0]
                cv.line(f, (x1, y1), (x2, y2), (0, 255, 0), 2)
            self._sortLines()
            print(self.detectBranches())


            #cv.imwrite("lines.png", f)
        cv.imshow("lines", f)
        k = cv.waitKey(5) & 0x5FF

        return 1


if __name__ == "__main__":
    from picture import capImage
    clf = Classifier()
    #frame = cv.imread("test.png")
    for i in range(10000):
        frame = capImage()
        clf.classify(frame)
