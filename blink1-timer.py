#!/usr/local/bin/python
import time
from blink1.blink1 import Blink1
import signal
import sys
import argparse

def signal_handler(sig, frame):
    print('\r\nExitting')
    b1.fade_to_rgb(500, 0, 0, 0)
    b1.close()
    sys.exit(0)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# PRE
signal.signal(signal.SIGINT, signal_handler)

# ARGS
parser = argparse.ArgumentParser(description=   'This program is a cycle timer with configureable cycle times. \
                                                Therefore the USB LED from https://blink1.thingm.com/ is used. \
                                                 By default work color is red and pause color is green. \
                                                 So the timer can be used as Pomodoro Timer, or with 50 \
                                                 minutes work and 10 minutes break, how I personally use it.')
parser.add_argument('-t', dest='time', type=int, nargs=1,required=True,
                    help='Time in minutes to work, LED stays green')
parser.add_argument('-p', dest='pause', type=int, nargs=1,required=True,
                    help='Time in minutes to rest, LED stays red')
args = parser.parse_args()

# Blink1 init
b1 = Blink1()

arg_time  = int(args.time[0])
arg_pause = int(args.pause[0])

while True:
    print "Entering loop with a worktime of " + str(arg_time) + " minutes and " + str(arg_pause) + " minutes break time."

    timetime_left = arg_time
    while timetime_left > 0 :
        b1.fade_to_rgb(500, 231, 0, 0)
        sys.stdout.write("Currently " + color.BOLD + str(timetime_left) + color.END + " minutes left for work            \r")
        sys.stdout.flush()
        time.sleep(60)
        timetime_left -= 1
        if timetime_left == 0 :
            print("\r\n Worktime ended. Take a break!")
            for i in range(1,40) :
                print ('\r\a')
                time.sleep(0.1)

    pausetime_left = arg_pause
    while pausetime_left > 0 :
        if pausetime_left == arg_pause:
            b1.writePatternLine(50,'red',1)
            b1.writePatternLine(50,'green',2)
            b1.writePatternLine(100,'black',3)
            b1.play(1,3,25)
            sys.stdout.write("Currently " + color.BOLD + str(pausetime_left) + color.END + "minutes left for pause           \r")
            sys.stdout.flush()
            time.sleep(55)
        else:
            b1.fade_to_rgb(500, 0, 231, 0)
            sys.stdout.write("Currently " + color.BOLD + str(pausetime_left) + color.END + "minutes left for pause           \r")
            sys.stdout.flush()
            time.sleep(60)

        pausetime_left -= 1
        if pausetime_left == 0 :
            print("\r\n Pause ended, start working again.")
            for i in range(1,40) :
                print ('\r\a')
                time.sleep(0.1)






