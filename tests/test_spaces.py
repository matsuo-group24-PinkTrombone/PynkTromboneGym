from dataclasses import dataclass

import numpy as np

from pynktrombonegym import spaces as ptspaces


def test_BaseSpace():
    bs = ptspaces.BaseSpace()

    d = bs.to_dict()
    assert type(d) is dict
    assert d == dict()
    try:
        ptspaces.BaseSpace.from_dict({"a": 0})
        raise AssertionError
    except TypeError:
        pass

    @dataclass
    class Space(ptspaces.BaseSpace):
        state1: float
        state2: int
        state3: str

    o = Space(1.0, 2, "3")
    assert o.to_dict() == {"state1": 1.0, "state2": 2, "state3": "3"}

    d = {"state1": 0.0, "state2": 1, "state3": "2"}
    o = Space.from_dict(d)
    assert o.state1 == 0.0
    assert o.state2 == 1
    assert o.state3 == "2"


def test_ObservationSpace():
    cls = ptspaces.ObservationSpace

    obs = cls(
        np.arange(100, dtype=float),
        np.arange(-100, 0, dtype=float),
        np.zeros(10),
        np.ones(10),
        np.array([400.0]),
        np.array([0.0]),
        np.array([0.5]),
        np.arange(10, dtype=float),
        np.arange(5, dtype=float),
    )

    assert np.all(obs.target_sound_wave == np.arange(100, dtype=float))
    assert np.all(obs.generated_sound_wave == np.arange(-100, 0, dtype=float))
    assert np.all(obs.target_sound_spectrogram == np.zeros(10))
    assert np.all(obs.generated_sound_spectrogram == np.ones(10))
    assert obs.frequency.item() == 400.0
    assert obs.pitch_shift.item() == 0.0
    assert obs.tenseness.item() == 0.5
    assert np.all(obs.current_tract_diameters == np.arange(10, dtype=float))
    assert np.all(obs.nose_diameters == np.arange(5, dtype=float))


def test_ActionSpace():
    cls = ptspaces.ActionSpace

    act = cls(
        np.array([0.0]),
        np.array([0.1]),
        np.array([0.2]),
        np.array([0.3]),
        np.array([0.4]),
        np.array([5]),
        np.array([0.6]),
        np.array([0.7]),
    )
    assert act.pitch_shift.item() == 0.0
    assert act.tenseness.item() == 0.1
    assert act.trachea.item() == 0.2
    assert act.epiglottis.item() == 0.3
    assert act.velum.item() == 0.4
    assert act.tongue_index.item() == 5
    assert act.tongue_diameter.item() == 0.6
    assert act.lips.item() == 0.7
