import RPi.GPIO as GPIO
import time

INACTIVE = 0
SETTLING = 1
SENDING_PULSE = 2
WAITING = 3
SENSING = 4

class SensorStateMachine:
    def __init__(self, outPin, inPin, onPulse):
        self._currentState = INACTIVE
        self._onPulse = onPulse
        self._outPin = outPin
        self._inPin = inPin
        self._timerStart = None

    def deactivate(self):
        self._currentState = INACTIVE
        self._pulseStart = None
        self._pulseEnd = None

    def settle(self):
        self._currentState = SETTLING
        GPIO.output(self._outPin, False)
        self._timerStart = time.time()

    def sendPulse(self):
        self._currentState = SENDING_PULSE
        GPIO.output(self._outPin, True)

    def finishPulse(self):
        self._currentState = WAITING
        GPIO.output(self._outPin, True)
    
    def sense(self):
        self._currentState = SENSING
        self._timerStart = time.time()

    def measure(self):
        pulse_duration = time.time() - self._timerStart
        distance = round(pulse_duration * 17150, 2)
        self._onPulse(distance)

    def cycle(self):
        if self._currentState == INACTIVE:
            self.settle()
        elif self._currentState == SETTLING:
            if time.time() - self._timerStart >= 0.25:
                self.sendPulse()
        elif self._currentState == SENDING_PULSE:
            if time.time() - self._timerStart >= 0.00001:
                self.finishPulse()
        elif self._currentState == WAITING:
            if GPIO.input(self._inPin) == 1:
                self.sense()
        elif self._currentState == SENSING:
            if GPIO.input(self._inPin) == 0:
                self.measure()
