import argparse
import random
from typing import Optional

import numpy as np
import sounddevice as sd


def generate_sine_wave(frequency: int, duration: int, sample_rate: int) -> np.ndarray:
    """
    Generate a sine wave of a given frequency and duration.

    Args:
        frequency   : Frequency of the sine wave in Hertz.
        duration    : Duration of the wave in seconds.
        sample_rate : Sample rate in samples per second.

    Returns:
        A numpy array containing the sine wave.
    """
    t = np.linspace(start=0, stop=duration, num=int(sample_rate * duration), endpoint=False)
    amplitude = np.iinfo(np.int16).max
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave.astype(np.int16)


def play_wave(wave: np.ndarray, sample_rate: int) -> None:
    """
    Play a given wave using sounddevice.

    Args:
        wave        : A numpy array containing the wave data.
        sample_rate : Sample rate in samples per second.
    """
    sd.play(wave, samplerate=sample_rate)
    sd.wait()  # Wait until the sound has finished playing


def write_wave_to_file(wave: np.ndarray, file_name: str, sample_rate: int) -> None:
    """
    Writes wave data into a WAV file.

    Args:
        wave        : ndarray of wave data. Note that the type defines also the type of the file, e.g. if it is np.int16
                      then it will write a 16bit int file.
        file_name   : Path and filename of the WAV file.
        sample_rate : Sampling rate in Hertz, e.g. 192000, of the data and file.
    """
    import scipy.io.wavfile
    scipy.io.wavfile.write(filename=file_name, rate=sample_rate, data=wave)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--low",
        type=int,
        default=15000,
        help="Lower bound of the uniformly generated random frequencies in Hz"
    )
    parser.add_argument(
        "--high",
        type=int,
        default=20000,
        help="Upper bound of the uniformly generated random frequencies in Hz"
    )
    parser.add_argument(
        "--number",
        type=int,
        default=10,
        help="How many frequencies to generate"
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=5,
        help="Duration in seconds of the sound wave per frequency. The overall length of sounds is number * duration."
    )
    parser.add_argument(
        "--save",
        type=str,
        default=None,
        help="File name to write the audio instead of playing it. This will create a WAV file, so you should use the "
             ".wav extension."
    )
    parser.add_argument(
        "--rate",
        type=int,
        default=192000,
        help="This is the sampling rate. Use high sampling rates (e.g. 192000) to capture the high frequencies. See "
             "https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem"
    )
    args = parser.parse_args()

    all_wave_data: Optional[np.ndarray] = None
    random_frequencies: list[int] = []

    # Generate sine wave
    for i in range(args.number):
        random_frequency = random.randint(args.low, args.high)
        one_frequency_wave = generate_sine_wave(
            frequency=random_frequency,
            duration=args.duration,
            sample_rate=args.rate,
        )
        random_frequencies.append(random_frequency)
        all_wave_data = \
            np.concatenate([all_wave_data, one_frequency_wave]) if all_wave_data is not None else one_frequency_wave

    print(f"Created random frequencies: {random_frequencies}")

    if args.save:
        write_wave_to_file(wave=all_wave_data, file_name=args.save, sample_rate=args.rate)
    else:
        play_wave(all_wave_data, sample_rate=args.rate)


if __name__ == "__main__":
    main()
