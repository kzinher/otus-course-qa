import pytest

@pytest.fixture
def test_b():
    return 1



def test_c(test_b):
    assert test_b == 1
