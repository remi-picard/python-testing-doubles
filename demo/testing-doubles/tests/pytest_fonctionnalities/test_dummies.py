def do_some_stuff(param1, param2):
    if param1 == 42:
        return False
    if param2 % param1 == 5:
        return True
    return None


def test_dummies():
    dummy = None
    assert not do_some_stuff(42, dummy)
