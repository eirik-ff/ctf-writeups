import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile 


# thanks ChatGPT
def frequency_to_note(frequency):
    A4_frequency = 440.0  # Frequency of A4 in Hz
    semitone_ratio = 2 ** (1 / 12.0)

    # Calculate the note number note_number = 12 * np.log2(frequency / A4_frequency) + 69

    # Round to the nearest integer
    note_number = round(note_number)

    # Map the note number to a note name
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_index = (note_number - 1) % 12
    octave = (note_number - 12) // 12

    note_name = note_names[note_index]

    return f"{note_name}{octave}"


def play_sine_wave(frequency, duration, sample_rate=44100):
    print(frequency_to_note(frequency))
    t = np.arange(int(sample_rate * duration)) / sample_rate
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    print(wave.shape)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()


def Beep(freq, dur_ms):
    play_sine_wave(freq, dur_ms * 1e-3)


def Sleep(dur_ms):
    time.sleep(dur_ms * 1e-3)


wave = np.zeros((1,))
sample_rate = 44100

def BuildBeep(freq, dur_ms):
    global wave, sample_rate

    duration = dur_ms * 1e-3
    frequency = freq
    t = np.arange(int(sample_rate * duration)) / sample_rate
    wave_beep = 0.5 * np.sin(2 * np.pi * frequency * t)

    wave = np.concatenate((wave, wave_beep))


def BuildSleep(dur_ms):
    global wave, sample_rate

    duration = dur_ms * 1e-3
    t = np.arange(int(sample_rate * duration)) / sample_rate
    wave_beep = np.zeros_like(t)

    wave = np.concatenate((wave, wave_beep))


def BuildPlay():
    global wave, sample_rate

    print("play", wave.shape)

    sd.play(wave, samplerate=sample_rate)
    sd.wait()


def BuildSave():
    global wave, sample_rate

    print("saving")

    scipy.io.wavfile.write("beep.wav", sample_rate, wave)


def beep1():
    # This is morse code
    Beep(800, 500)
    # . = E
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 500)
    # --. = G
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 500)
    # --. = G
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 500)
    Beep(800, 500)
    Beep(800, 500)
    # -... = B
    Sleep(1000)
    Beep(800, 500)
    # . = E
    Sleep(1000)
    Beep(800, 500)
    # . = E
    Sleep(1000)
    Beep(800, 500)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 500)
    # .--. = P
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 500)
    Beep(800, 500)
    Beep(800, 500)
    # -... = B
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 1500)
    # --- = O
    Sleep(1000)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 1500)
    # --- = O
    Sleep(1000)
    Beep(800, 500)
    Beep(800, 1500)
    Beep(800, 1500)
    Beep(800, 500)
    # .--. = P
    Sleep(1000)

def beep2():
    BuildBeep(738, 200)
    BuildSleep(20)
    BuildBeep(738, 200)
    BuildBeep(1108, 200)
    BuildBeep(986, 200)
    BuildSleep(20)
    BuildBeep(880, 200)
    BuildSleep(20)
    BuildBeep(830, 200)
    BuildSleep(20)
    BuildBeep(830, 200)
    BuildBeep(830, 200)
    BuildBeep(986, 200)
    BuildSleep(20)
    BuildBeep(880, 200)
    BuildBeep(830, 200)
    BuildBeep(738, 200)
    BuildSleep(20)
    BuildBeep(738, 200)
    BuildBeep(1760, 200)
    BuildBeep(1660, 200)
    BuildBeep(1760, 200)
    BuildBeep(1660, 200)
    BuildBeep(1760, 200)
    BuildBeep(738, 200)
    BuildSleep(20)
    BuildBeep(738, 200)
    BuildBeep(1760, 200)
    BuildBeep(1660, 200)
    BuildBeep(1760, 200)
    BuildBeep(1760, 200)
    BuildBeep(1660, 200)

def beep3():
    BuildBeep(800, 200)
    BuildBeep(800, 200)
    BuildBeep(800, 200)
    BuildBeep(800, 200)
    BuildBeep(1108, 200)
    BuildBeep(1108, 200)
    BuildBeep(1108, 200)
    BuildBeep(1108, 200)
    BuildBeep(986, 200)
    BuildBeep(986, 200)
    BuildBeep(986, 200)
    BuildBeep(986, 200)
    BuildBeep(1318, 200)
    BuildBeep(1318, 200)
    BuildBeep(1318, 200)
    BuildBeep(1318, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(1478, 200)
    BuildBeep(986, 200)
    BuildBeep(800, 200)
    BuildBeep(830, 200)
    BuildBeep(658, 200)


def beep_function():
    # Coffin dance! 
    beep2()
    beep2()
    beep2()
    beep3()
    beep2()
    beep2()
    beep2()
    beep3()


if __name__ == "__main__":
    beep_function()
    BuildSave()

