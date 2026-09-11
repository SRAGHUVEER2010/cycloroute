import pytest

from cycloroute.wind import (
    velocity_vector,
    relative_velocity,
    magnitude_relative_velocity,
    relative_direction,
    relative_wind
)

def test_magnitude_relative_velocity():
    result = magnitude_relative_velocity(3, 4)

    assert result == 5

def test_velocity_vector_north():
    result = velocity_vector(10, 0)

    assert result == pytest.approx((0, 10))


def test_velocity_vector_east():
    result = velocity_vector(10, 90)

    assert result == pytest.approx((10, 0))


def test_velocity_vector_south():
    result = velocity_vector(10, 180)

    assert result == pytest.approx((0, -10))


def test_velocity_vector_west():
    result = velocity_vector(10, 270)

    assert result == pytest.approx((-10, 0))


def test_relative_velocity():
    result = relative_velocity(10, 5, 3, 2)

    assert result == pytest.approx((7, 3))


def test_of_magnitude_relative_velocity():
    result = magnitude_relative_velocity(3, 4)

    assert result == pytest.approx(5)


def test_relative_direction_north():
    result = relative_direction(0, 10)

    assert result == pytest.approx(0)


def test_relative_direction_east():
    result = relative_direction(10, 0)

    assert result == pytest.approx(90)


def test_relative_direction_south():
    result = relative_direction(0, -10)

    assert result == pytest.approx(180)


def test_relative_direction_west():
    result = relative_direction(-10, 0)

    assert result == pytest.approx(270)


def test_relative_direction_diagonal():
    result = relative_direction(3, 4)

    assert result == pytest.approx(36.8699, abs=0.001)
def test_relative_wind_tailwind():
    # wind and cyclist both heading north (0°), wind is 5 km/h faster
    result = relative_wind(20, 0, 15, 0)

    assert result == pytest.approx((5.0, 0.0))


def test_relative_wind_headwind():
    # wind blowing from the south (180°) straight at a cyclist heading north (0°)
    # cyclist moving north = wind vector (0, 10), wind vector (0, -10)
    # relative = wind - cyclist = (0, -20) -> magnitude 20, hitting head-on
    result = relative_wind(10, 180, 10, 0)

    assert result == pytest.approx((20.0, 180.0))
