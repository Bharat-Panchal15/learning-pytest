from main import get_weather
import pytest

def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(20) == "cold"