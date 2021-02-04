# Stub méthode
import math


def get_cosinus(x):
    return math.cos(x)


def test_stubs_math_cos(monkeypatch):
    def stub_cos(*args, **kwargs):
        return args[0]
    monkeypatch.setattr(math, 'cos', stub_cos)
    assert get_cosinus(5) == 5


# Stub classe
import datetime
def which_day():
    today = datetime.date.today()
    return today.day


def test_stubs_datetime_date(monkeypatch):
    class DateStub:
        @classmethod
        def today(cls):
            class Object(object):
                pass
            today = Object()
            today.day = 9
            return today

    monkeypatch.setattr(datetime, 'date', DateStub)
    assert which_day() == 9
