import RPi.GPIO as GPIO
import time
import os
from SensorStateMachine import SensorStateMachine, WAITING, SENSING, INACTIVE

SENSORS = [
  (18, 23, "do"),
  (24, 25, "re"),
  (12, 16, "mi"),
  (20, 21, "fa"),
  (19, 26, "sol")
]

def makeSound(soundName):
  def emitSound(distance):
    if distance < 20:
      os.system("omxplayer {}.wav &".format(soundName))

  return emitSound

def buildMachines(sensors):
  return [SensorStateMachine(sound, outPin, inPin, makeSound(sound)) for outPin, inPin, sound in sensors]

def setup(sensors):
  GPIO.setmode(GPIO.BCM)

  for outPin, inPin, sound in sensors:
    GPIO.setup(outPin,GPIO.OUT)
    GPIO.setup(inPin,GPIO.IN)

  return buildMachines(sensors)


def loop(machines):

  try:
    while True:
      for machine in machines:
        machine.cycle()
  except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()


machines = setup(SENSORS)
loop(machines)