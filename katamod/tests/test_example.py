from nose.tools import assert_equal
from nose.tools import assert_not_equal


def test_equal():
    assert_equal(False, False)

def test_not_equal():
    assert_not_equal(False, True)
