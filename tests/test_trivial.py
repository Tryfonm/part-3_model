import pytest

@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1
