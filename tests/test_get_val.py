import pytest

from utils.dicts import get_val


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


def test_get_value(data):
    assert get_val(data, 'fire') == 'git'
    assert get_val(data, 'vcs') == 'mercurial'
    assert get_val({}, 'ssd') == 'git'
    assert get_val({}, "vcs", 'bazaar') == 'bazaar'
