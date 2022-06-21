import sys
from controller import Controller

default_steps = 200
control = Controller()

print(sys.argv)
if len(sys.argv) < 2:
    steps = default_steps
    print("Using default number of steps: ", default_steps)
    print("To specify the number of steps run: python3 remote.py <number_of_steps>")
else:
    steps = int(sys.argv[1])
    print("Number of steps was specified to be: ", sys.argv[1])

for i in range(100000):
    inp = input()
    if inp == "w":
        control.step_forward(steps)
    elif inp == "s":
        control.step_backwards(steps)
    elif inp == "a":
        control.rotate_counterclockwise(steps)
    elif inp == "d":
        control.rotate_clockwise(steps)
    else:
        print(inp, " is not a valid input. Use w, a, s, d to control the robot.")
