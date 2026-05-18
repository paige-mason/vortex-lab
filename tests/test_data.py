import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd

from data import (generate_day, estimate_wind_speed, adjust_intensity)

def test_generate_day():
    day = generate_day()
    assert 1 <= day <= 28

def test_estimate_wind_speed():
    wind = estimate_wind_speed(3)
    assert 136 <= wind <= 165

def test_adjust_intensity():
    ef = adjust_intensity(2, 93, 86)
    assert 0 <= ef <= 5