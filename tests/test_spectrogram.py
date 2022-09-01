import numpy as np

from pynktrombonegym import spectrogram as spct


def test_calc_rfft_channel_num():
    f = spct.calc_rfft_channel_num
    assert f(1024) == 513
    assert f(256) == 129
    assert f(400) == 201
    assert f(501) == 251


def test_calc_target_sound_spectrogram_length():
    f = spct.calc_target_sound_spectrogram_length
    assert f(512, 1024, 256) == 3
    assert f(1024, 1024, 256) == 5
    assert f(1024, 512, 128) == 9


def test_stft():
    f = spct.stft
    cf = spct.calc_rfft_channel_num
    lf = spct.calc_target_sound_spectrogram_length
    wave = np.sin(np.linspace(0, 2 * np.pi, 1024))
    out = f(wave, 1024, 256)
    assert out.dtype == np.complex128
    assert out.shape == (lf(len(wave), 1024, 256), cf(1024))
