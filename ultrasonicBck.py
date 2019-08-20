import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)

TRIG = 18 
ECHO = 23
TRIG2 = 24 
ECHO2 = 25
TRIG3 = 12 
ECHO3 = 16
TRIG4 = 20 
ECHO4 = 21
TRIG5 = 19 
ECHO5 = 26

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(TRIG4,GPIO.OUT)
GPIO.setup(TRIG5,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(ECHO4,GPIO.IN)
GPIO.setup(ECHO5,GPIO.IN)
try:
    while True:

        GPIO.output(TRIG, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.25)

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

	#Ultrasonic 2
        GPIO.output(TRIG2, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.25)

        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)

        while GPIO.input(ECHO2)==0:
          pulse_start2 = time.time()

        while GPIO.input(ECHO2)==1:
          pulse_end2 = time.time()

        pulse_duration2 = pulse_end2 - pulse_start2

        distance2 = pulse_duration2 * 17150

        distance2 = round(distance2, 2)

        print "Distance ultrasonic 2:",distance2,"cm"

        if distance2 < 20:
            GPIO.output(27, True)
	    os.system('omxplayer re.wav &')
        else:
            GPIO.output(27, False)

	#Ultrasonic 3
        GPIO.output(TRIG3, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.25)

        GPIO.output(TRIG3, True)
        time.sleep(0.00001)
        GPIO.output(TRIG3, False)

        while GPIO.input(ECHO3)==0:
          pulse_start3 = time.time()

        while GPIO.input(ECHO3)==1:
          pulse_end3 = time.time()

        pulse_duration3 = pulse_end3 - pulse_start3

        distance3 = pulse_duration3 * 17150

        distance3 = round(distance3, 2)

        print "Distance ultrasonic 3:",distance3,"cm"

        if distance3 < 20:
            GPIO.output(27, True)
	    os.system('omxplayer fa.wav &')
        else:
            GPIO.output(27, False)


	#Ultrasonic 4
        GPIO.output(TRIG4, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.25)

        GPIO.output(TRIG4, True)
        time.sleep(0.00001)
        GPIO.output(TRIG4, False)

        while GPIO.input(ECHO4)==0:
          pulse_start4 = time.time()

        while GPIO.input(ECHO4)==1:
          pulse_end4 = time.time()

        pulse_duration4 = pulse_end4 - pulse_start4

        distance4 = pulse_duration4 * 17150

        distance4 = round(distance4, 2)

        print "Distance ultrasonic 4:",distance4,"cm"

        if distance4 < 20:
            GPIO.output(27, True)
	    os.system('omxplayer sol.wav &')
        else:
            GPIO.output(27, False)

	#Ultrasonic 5
        GPIO.output(TRIG5, False)
        print "Waiting For Sensor To Settle"
        time.sleep(0.25)

        GPIO.output(TRIG5, True)
        time.sleep(0.00001)
        GPIO.output(TRIG5, False)

        while GPIO.input(ECHO5)==0:
          pulse_start5 = time.time()

        while GPIO.input(ECHO5)==1:
          pulse_end5 = time.time()

        pulse_duration5 = pulse_end5 - pulse_start5

        distance5 = pulse_duration5 * 17150

        distance5 = round(distance5, 2)

        print "Distance ultrasonic 5:",distance5,"cm"

        if distance5 < 20:
            GPIO.output(27, True)
	    os.system('omxplayer mi.wav &')
        else:
            GPIO.output(27, False)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
