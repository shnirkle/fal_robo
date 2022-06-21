from stepper import StepperMotor

"""
Provides functions to control the robots movements.
"""


class Controller:
    def __init__(self):
        self.enable_pin = 0
        self.step_pin1 = 1
        self.step_pin2 = 8
        self.dir_pin1 = 7
        self.dir_pin2 = 25
        self.mode_pin = 20
        self.stepper1 = StepperMotor(self.enable_pin,
                                     self.step_pin1,
                                     self.dir_pin1)
        self.stepper2 = StepperMotor(self.enable_pin,
                                     self.step_pin2,
                                     self.dir_pin2)

    def step_forward(self, steps: int):
        self.stepper1.enable(True)
        self.stepper1.run(steps, True)
        self.stepper2.run(steps, False)
        self.stepper1.enable(False)

    def step_backwards(self, steps: int):
        self.stepper1.enable(True)
        self.stepper1.run(steps, False)
        self.stepper2.run(steps, True)
        self.stepper1.enable(False)

    def rotate_clockwise(self, steps: int):
        self.stepper1.enable(True)
        self.stepper1.run(steps, False)
        self.stepper2.run(steps, False)
        self.stepper1.enable(False)

    def rotate_counterclockwise(self, steps: int):
        self.stepper1.enable(True)
        self.stepper1.run(steps, True)
        self.stepper2.run(steps, True)
        self.stepper1.enable(False)
