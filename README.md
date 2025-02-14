# Micebuster
<div style="text-align:center"><img src="mouse.png" alt="Mouse leaving the house"/><br />
To get rid of mice and rats without killing them.</div>

## Background
Mice ant rats can hear ultrasound (e.g. sound above a frequency of 20000Hz), but humans
can not. Apparently, mice and rats do not like it if you play randomly pitched sound
pulses between 22kHz and 35hHz. So you actually can use audio to get rid of them. If
you use this over days or weeks, they will simply go away and find another place to live.

However, since mice may become accustomed to a single frequency over time, the frequency
should be varied.

This application is designed exactly for that: randomly pitched sound at high frequencies.

## Warning
**Never use this near dogs, cats or any other pets. Also, there is research showing ultrasound
frequencies might sometimes still be sensed by humans or could cause headaches.**

**Never use too loud sounds, especially in the frequencies of the human ear. You might cause damage to the ear.**

## Requirements
### Hardware
You need a speaker that has enough power (dB) also at a range between 22kHz and 35kHz.
I use a HomePod Mini for this, although it seems to have quite a falloff already at 17-20kHz (
https://www.rtings.com/speaker/reviews/apple/homepod-mini ), so I use as default a frequency between 15kHz and 20kHz.

## Installation
- If you do not have Conda already, get it from, e.g., here: https://docs.anaconda.com/free/anaconda/install/index.html
- On Mac you need to do: `brew install portaudio`
- `conda env create -f environment.yml`

## Run
- `conda activate micebuster`
- `python audio_generator.py`

If you want to store the generated audio wave in a file, just add the flag `--save [filename]` where you replace
`[filename]` with the target wave file, e.g. `random_15kHz_to_20kHz.wav`.

You can also define the base frequency (`--low [frequency Hz]`) and the range (`--high [frequency Hz]`), where the
range between low and high define the frequency range for the uniformly generated random frequencies.
