import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 42])
def test_parametrize(number):
    assert number > 0


@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (1, 1, 2),
    (1, -1, 0),
])
def test_parametrize(a, b, expected):
    assert a + b == expected
