import pytest

from cycloroute.physics import road_gradient, gravitational_resistance , rolling_resistance


def test_road_gradient_zero():
    result = road_gradient(0)

    assert result == 0


def test_road_gradient_uphill():
    result = road_gradient(5)

    assert result == pytest.approx(0.0499584)


def test_road_gradient_downhill():
    result = road_gradient(-5)

    assert result == pytest.approx(-0.0499584)


def test_gravitational_resistance_flat():
    result = gravitational_resistance(70, 0)

    assert result == pytest.approx(0)


def test_gravitational_resistance_uphill():
    angle = road_gradient(5)
    result = gravitational_resistance(70, angle)

    assert result == pytest.approx(34.3, abs=0.1)


def test_gravitational_resistance_downhill():
    angle = road_gradient(-5)
    result = gravitational_resistance(70, angle)

    assert result == pytest.approx(-34.3, abs=0.1)
def test_rollingresisttest():

    result = rolling_resistance(0 , 70, 0.005)
    assert result == pytest.approx(3.4335)

