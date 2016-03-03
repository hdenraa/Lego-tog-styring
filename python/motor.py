#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(3)
currentSpeed=0
def setSpeed(finalSpeed=None, delta=None):
        global currentSpeed
        if finalSpeed is not None:
                print "Final Speed"
                endSpeed=finalSpeed
        elif delta is not None:
                print "Delta"
                endSpeed=(currentSpeed +  delta)
        if endSpeed > 255:
                print "Max Speed Forward"
                endSpeed=255
        if endSpeed < -255:
                print "Max Speed Backward"
                endSpeed=-255
        prev =currentSpeed

        if endSpeed >= currentSpeed:
                step=1
        else:
                step=-1
        for i in range(currentSpeed, endSpeed, step):
                if prev == 0 and i == 1:
                        print "Switch to forward"
                        myMotor.run(Adafruit_MotorHAT.FORWARD)
                elif prev == 0 and i == -1:
                        print "Switch to backward"
                        myMotor.run(Adafruit_MotorHAT.BACKWARD)
                myMotor.setSpeed(abs(i))
                print "current Speed: " + str(i)
                time.sleep(0.1)
                prev=i
                currentSpeed=i

if __name__ == '__main__':
    setSpeed(finalSpeed=100)
    setSpeed(delta=-100)
    print "Done"
