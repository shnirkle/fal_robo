from controller import Controller
import RPi.GPIO as GPIO
from imReco.picture import capImage
from imReco.classifier import Classifier


clf = Classifier()
control = Controller()
steps = 200

while True:
    frame = capImage()
    branches = clf.classify(frame)
    if branches[0] == 1:
        if branches[1] == 5:
            control.rotate_clockwise(steps//2)
        if branches[1] == 6:
            control.rotate_counterclockwise(steps//2)
    control.step_forward(steps)
