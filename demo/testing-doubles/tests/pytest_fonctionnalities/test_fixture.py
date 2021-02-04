import pytest


@pytest.fixture()
def ma_fixture():
    return "Hello !"


def test_fixture(ma_fixture):
    assert ma_fixture == "Hello !"
