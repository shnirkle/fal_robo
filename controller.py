import stepper
from stepper import StepperMotor

"""
Provides functions to control the robots movements.
"""


class Controller:
    def __init__(self):
        self.enable_pin = 2
        self.step_pin1 = 22
        self.step_pin2 = 24
        self.dir_pin1 = 27
        self.dir_pin2 = 23
        self.mode_pin = 20
        self.stepper1 = StepperMotor(self.enable_pin,
                                     self.step_pin1,
                                     self.dir_pin1)
        self.stepper2 = StepperMotor(self.enable_pin,
                                     self.step_pin2,
                                     self.dir_pin2)

    def step_forward(self, steps: int):
        self.stepper1.enable(True)
        stepper.run_steppers(steps, ((self.stepper1, True), (self.stepper2, False)))
        # self.stepper1.run(steps, True)
        # self.stepper2.run(steps, False)
        self.stepper1.enable(False)

    def step_backwards(self, steps: int):
        self.stepper1.enable(True)
        stepper.run_steppers(steps, ((self.stepper1, False), (self.stepper2, True)))
        # self.stepper1.run(steps, False)
        # self.stepper2.run(steps, True)
        self.stepper1.enable(False)

    def rotate_clockwise(self, steps: int):
        self.stepper1.enable(True)
        stepper.run_steppers(steps, ((self.stepper1, False), (self.stepper2, False)))
        # self.stepper1.run(steps, False)
        # self.stepper2.run(steps, False)
        self.stepper1.enable(False)

    def rotate_counterclockwise(self, steps: int):
        self.stepper1.enable(True)
        stepper.run_steppers(steps, ((self.stepper1, True), (self.stepper2, True)))
        # self.stepper1.run(steps, True)
        # self.stepper2.run(steps, True)
        self.stepper1.enable(False)
