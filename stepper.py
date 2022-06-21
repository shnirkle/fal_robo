import RPi.GPIO as GPIO
from time import sleep

"""
Modified Version of the drv8825 Stepper Library from https://github.com/dimschlukas/rpi_python_drv8825
"""


class StepperMotor:
    def __init__(self, enable_pin, step_pin, dir_pin):
        self.enable_pin = enable_pin
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        self.delay = .0005

    def enable(self, enable):
        GPIO.output(self.enable_pin, not enable)

    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(self.delay)
