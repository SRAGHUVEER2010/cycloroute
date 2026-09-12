import pytest

from cycloroute.wind import (
    velocity_vector,
    relative_velocity,
    magnitude_relative_velocity,
    relative_direction,
    relative_wind,
    speed_unit_conversion,
)


def test_magnitude_relative_velocity():
    result = magnitude_relative_velocity(3, 4)

    assert result == pytest.approx(5)


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
    # Wind and cyclist both heading north.
    # Wind = 20 km/h, cyclist = 15 km/h.
    # Relative speed = 5 km/h = 1.388888... m/s
    result = relative_wind(20, 0, 15, 0)

    assert result == pytest.approx((1.3888888889, 0.0))


def test_relative_wind_headwind():
    # Wind from south toward north-facing cyclist.
    # Wind = 10 km/h southward, cyclist = 10 km/h northward.
    # Relative speed = 20 km/h = 5.555555... m/s
    result = relative_wind(10, 180, 10, 0)

    assert result == pytest.approx((5.5555555556, 180.0))


def test_speed_conversion():
    result = speed_unit_conversion(18)

    assert result == pytest.approx(5)


def test_speed_conversion_36_kmh():
    result = speed_unit_conversion(36)

    assert result == pytest.approx(10)


def test_speed_conversion_zero():
    result = speed_unit_conversion(0)

    assert result == pytest.approx(0)
