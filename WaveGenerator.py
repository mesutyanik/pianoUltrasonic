import pyaudio
import numpy as np
import time

class WaveGenerator:
    def __init__(self):
        self._freq = 0
        self._amplitude = 0
        self._p = pyaudio.PyAudio()
        self._timer = time.time()

    def open(self):
        self._fs = 44100

        self._stream = self._p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=self._fs,
                output=True)

    def set_freq(self, freq):
        print("NEW FREQ " + freq)
        this._freq = freq

    def set_amplitude(self, amplitude):
        print("NEW AMP " + amplitude)
        this._amplitude = amplitude

    def emit_sound(self, duration):
        print("CURR AMPLITUDE" + str(self._amplitude))
        print("CURR FREQ" + str(self._freq))
        samples = (np.sin(2*np.pi*np.arange(self._fs*duration)*self._freq/self._fs)).astype(np.float32)
        self._stream.write(self._amplitude*samples)

    def cycle(self):
        current_time = time.time()
        if current_time - self._timer >= 0.25:
            self.emit_sound(0.25)
            self._timer = time.time()