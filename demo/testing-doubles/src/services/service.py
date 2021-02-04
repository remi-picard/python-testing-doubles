from services import dao


def get_data(id):
    return dao.get_data(id)


def get_all_data():
    return dao.get_all_data()