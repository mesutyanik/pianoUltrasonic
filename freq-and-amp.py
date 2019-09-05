import RPi.GPIO as GPIO
import time
import os
from SensorStateMachine import SensorStateMachine
from WaveGenerator import WaveGenerator

SENSORS = [
  (18, 23, "do"),
  (24, 25, "re"),
  (12, 16, "mi"),
  (20, 21, "fa"),
  (19, 26, "sol")
]

def change_freq(wave_generator):
  min_freq, max_freq = 200, 600

  def change_freq_from_distance(distance):
    current_freq = max_freq - 10 * distance
    if current_freq < min_freq:
      current_freq = min_freq
    wave_generator.set_freq(current_freq)

  return change_freq_from_distance


def change_amplitude(wave_generator):
  def change_amplitude_from_distance(distance):
    current_amplitude = 1 - (distance / 20)
    if current_amplitude < 0:
      current_amplitude = 0
    wave_generator.set_amplitude(current_amplitude)

  return change_amplitude_from_distance

def buildMachines(sensors, wave_generator):
  machines = []
  outPin, inPin, sound = sensors[0]
  machines.append(SensorStateMachine(sound, outPin, inPin, change_freq(wave_generator)))
  outPin, inPin, sound = sensors[1]
  machines.append(SensorStateMachine(sound, outPin, inPin, change_amplitude(wave_generator)))
  return machines

def setup(sensors, wave_generator):
  GPIO.setmode(GPIO.BCM)

  for outPin, inPin, sound in sensors:
    GPIO.setup(outPin,GPIO.OUT)
    GPIO.setup(inPin,GPIO.IN)
  
  wave_generator.open()

  return buildMachines(sensors, wave_generator)


def loop(machines, wave_generator):

  try:
    while True:
      for machine in machines:
        machine.cycle()
      wave_generator.cycle()
  except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    GPIO.cleanup()


wave_generator = WaveGenerator()
machines = setup(SENSORS[0:2], wave_generator)
loop(machines, wave_generator)