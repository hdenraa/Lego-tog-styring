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
        if finalSpeed is not None:
                endSpeed=finalSpeed
        elif delta is not None:
                endSpeed=(currentSpeed +  delta)
        if endSpeed > 255:
                endSpeed=255
        if endSpeed < -255:
                endSpeed=-255
        prev =currentSpeed
        for i in range(currentSpeed, endSpeed):
                if prev == 0 and i == 1:
                        myMotor.run(Adafruit_MotorHAT.FORWARD)
                elif prev == 0 and i == -1:
                        myMotor.run(Adafruit_MotorHAT.BACKWARD)
                myMotor.setSpeed(abs(i))
                time.sleep(0.1)
                prev=i

if __name__ == '__main__':
    setSpeed(finalSpeed=100)
    setSpeed(delta=-100)
    print "Done"
