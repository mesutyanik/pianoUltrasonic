import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)

TRIG = 19 
ECHO = 26

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:

        GPIO.output(TRIG, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.5)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print "Distance:",distance,"cm"
        if distance < 20:
            GPIO.output(27, True)
	    os.system('omxplayer do.wav &')
        else:
            GPIO.output(27, False)


except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
