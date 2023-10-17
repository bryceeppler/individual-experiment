import numpy as np
import simpleaudio as sa


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


def main():
    # Play a 1-second tone at 440 Hz
    play_tone(440, 1)

if __name__ == "__main__":
    main()