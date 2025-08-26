import numpy as np
import librosa
import soundfile as sf


def load_audio(path):
    y, sr = librosa.load(path)

    print(y)
    print(sr)

    return (y, sr)


def write_audio(filename, y, sr):
    sf.write(filename, y, sr, subtype="PCM_24")


def main():
    """Test loading an audio file as waveform and sample rate, convert back to audio file"""
    # file = librosa.example("nutcracker")
    # write_audio("Nutcracker.wav", *load_audio(file))


if __name__ == "__main__":
    main()
