#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

# GPIO setup
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

# setup gpio for echo & trig
echopin = [18,24]
trigpin = [23,25]
 
for j in range(2):
    GPIO.setup(trigpin[j], GPIO.OUT)
    GPIO.setup(echopin[j], GPIO.IN)
    print j, echopin[j], trigpin[j]
    print " "
    


# Get reading from HC-SR04   
def ping(echo, trig):
    
    GPIO.output(trig, False)
    # Allow module to settle
    time.sleep(0.5)
    # Send 10us pulse to trigger
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    # time difference between start and arrival
    pulse_duration = pulse_end - pulse_start
    # mutiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    
    return distance    
    
   
