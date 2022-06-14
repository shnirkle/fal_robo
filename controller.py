from rpi_python_drv8825.stepper import StepperMotor

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
        self.step_type = '1/4'
        self.fullstep_delay = 'fu'
        self.stepper1 = StepperMotor(self.enable_pin,
                                     self.step_pin1,
                                     self.dir_pin1,
                                     self.mode_pin,
                                     self.step_type,
                                     self.fullstep_delay)
        self.stepper2 = StepperMotor(self.enable_pin,
                                     self.step_pin2,
                                     self.dir_pin2,
                                     self.mode_pin,
                                     self.step_type,
                                     self.fullstep_delay)

    def step_forward(self, steps: int):
        self.stepper1.run(steps, True)
        self.stepper2.run(steps, False)

    def step_backwards(self, steps: int):
        self.stepper1.run(steps, False)
        self.stepper2.run(steps, True)

    def rotate_clockwise(self, steps: int):
        self.stepper1.run(steps, False)
        self.stepper2.run(steps, False)

    def rotate_counterclockwise(self, steps: int):
        self.stepper1.run(steps, True)
        self.stepper2.run(steps, True)
