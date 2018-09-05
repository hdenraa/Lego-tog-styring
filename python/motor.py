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

        if endSpeed >= currentSpeed:
                step=1
        else:
                step=-1

        if currentSpeed == 0:
                endSpeed = step *125

        if abs(endSpeed) < 125:
                endSpeed = 0

        if currentSpeed == 0 and step == 1:
                print "Switch to forward"
                myMotor.run(Adafruit_MotorHAT.FORWARD)
        elif currentSpeed == 0 and step == -1:
                print "Switch to backward"
                myMotor.run(Adafruit_MotorHAT.BACKWARD)
        if endSpeed == 125:
                loopSpeed=65
                while loopSpeed < 125:
                        myMotor.setSpeed(abs(loopSpeed))
                        time.sleep(0.05)
                        loopSpeed += 1
        else:
                myMotor.setSpeed(abs(endSpeed))
        currentSpeed=endSpeed
        return endSpeed
if __name__ == '__main__':
    setSpeed(finalSpeed=100)
    setSpeed(delta=-100)
    print "Done"
