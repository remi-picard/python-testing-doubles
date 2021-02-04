import unittest.mock as mock

from services import service, dao


def test_get_data_mock_patch_with():
    with mock.patch("services.dao.get_data") as mock_dao_get_data:
        mock_dao_get_data.return_value = 41
        ret = service.get_data(1)
        assert ret == 41


@mock.patch("services.dao.get_data")
def test_get_data_mock_patch_decorator(mock_dao_get_data):
    mock_dao_get_data.return_value = 41
    ret = service.get_data(1)
    assert ret == 41


def test_get_data_monkeypatch(monkeypatch):
    def get_data(x):
        return 41
    monkeypatch.setattr(dao, "get_data", get_data)
    ret = service.get_data(1)
    assert ret == 41


def test_get_data_monkeypatch_lambda(monkeypatch):
    monkeypatch.setattr(dao, "get_data", lambda x: 41)
    ret = service.get_data(1)
    assert ret == 41
