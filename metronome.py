#!/usr/bin/env

"""A simple metronome app in Python

Latency will be an issue using Python over compiled and lower level languages with better OS integration.
This is simply a proof of concept and practice project idea. Could expand to synchronous threads later but will
still suffer more than other languages.
"""

import os
import time
import simpleaudio as sa
# import asyncio


def main():
    def calculate_tempo(bpm):
        """Calculate the time interval depending on input tempo. - Click interval = 60 seconds / Beats per minute
        60s / 60bpm = 1s (60bpm is one click every second), 60s / 120bpm = 0.5s; 60s / 30bpm = 2s"""
        interval = 60 / bpm
        return interval

    def beat():
        click.play()

    def interval():
        nonlocal next_beat_time
        next_beat_time += pause
        time_diff = next_beat_time - time.perf_counter()
        if time_diff > 0:
            time.sleep(time_diff)   # time.sleep gives inaccurate pauses, as it does not factor in time taken up by
        else:                       # other system requirements and code executions. Using an 'expected' delay time
            print("slowing")        # helps align it (though still imperfectly)

    file_path = os.path.dirname(__file__) + r'\media\click.wav'  # Gets script directory + hardcoded subdirectory
    click = sa.WaveObject.from_wave_file(file_path)
    tempo = int(input('BPM = '))
    pause = calculate_tempo(tempo)
    next_beat_time = time.perf_counter()
    beat()

    while True:
        interval()
        beat()
    # Play Beat() > Calculate next beat time > Calculate difference to compensate lag
    # Call current time directly avoids delays
    # Time_delay sleep adjusted for time difference if more than 0


if __name__ == '__main__':
    main()
