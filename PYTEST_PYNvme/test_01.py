from pytest import mark
import pytest

@mark.exercise1
def test_exercise():
    assert True

print('hi am there')


def test_exampleassertion():
    with pytest.raises(Exception):
        assert(1/0)