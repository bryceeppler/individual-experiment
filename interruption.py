import numpy as np
import simpleaudio as sa
import tkinter as tk
from tkinter import messagebox
import schedule
import time
import random
import datetime

def play_tone(frequency, duration):
    """
    Play tone at frequency in Hz for duration seconds
    Adapted from https://simpleaudio.readthedocs.io/en/latest/tutorial.html
    """
    sample_rate = 44100
    # get timesteps for each sample
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # generate sine wave note
    note = np.sin(frequency * t * 2 * np.pi) 
    # normalize to 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Play the audio on the default output
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def show_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Interruption time", "Get interrupted bro!")
    root.destroy()

def interrupt():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global num_interruptions
    num_interruptions += 1
    print(f"Interruption number {num_interruptions} at {timestamp}")
    play_tone(440, 1)
    show_popup()

def run_interruption():
    interrupt()
    schedule.clear()
    schedule_interruption()

def schedule_interruption():
    # interval = 1.5 + random.uniform(-1, 1) # between 4-6 minutes
    interval = 0.1
    schedule.every(interval).minutes.do(run_interruption)

# Schedule first interruption
schedule_interruption()

num_interruptions = 0
start_timestamp = datetime.datetime.now()

while True:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Time elapsed: {datetime.datetime.now() - start_timestamp}")
    schedule.run_pending()
    time.sleep(1)