import unittest.mock as mock

from services import service, dao


@mock.patch("services.dao.get_data", wraps=dao.get_data)
def test_get_data_spy(spy_dao_get_data):
    ret = service.get_data(1)
    spy_dao_get_data.assert_called_with(1)
    assert ret == 42


@mock.patch("services.dao.get_all_data", wraps=dao.get_all_data)
def test_get_data_spy_mocked(spy_get_all_data):
    spy_get_all_data.return_value = [41]
    ret = service.get_all_data()
    spy_get_all_data.assert_called_with()
    assert ret == [41]
