import pytest

from lines import rotate


def ranger(a, b):
    step = 1 if b > a else -1
    return range(a, b, step)


@pytest.mark.parametrize('a, b', [
    (2, 5),
    (5, 2),
    (-2, 2),
    (2, -2),
    (-5, -2),
    (-2, -5),
])
def test_ranger(a, b):
    result = ranger(a, b)
    assert abs(a - b) == len(result)
    assert a in result


@pytest.mark.parametrize('p, expected', [
    # top
    pytest.param([4, 0], [5, 0], id='top'),
    pytest.param([4, 1], [5, 1], id='mid top'),
    # right
    pytest.param([7, 4], [7, 5], id='right'),
    pytest.param([6, 4], [6, 5], id='mid right'),
    # bottom
    pytest.param([5, 7], [4, 7], id='bottom'),
    pytest.param([5, 6], [4, 6], id='mid-bottom'),
    # left
    pytest.param([0, 5], [0, 4], id='left'),
    pytest.param([1, 5], [1, 4], id='mid-left'),
    # corners
    pytest.param([0, 0], [1, 0], id='top-left'),
    pytest.param([7, 0], [7, 1], id='top-right'),
    pytest.param([7, 7], [6, 7], id='bottom-right'),
    pytest.param([0, 7], [0, 6], id='bottom-left'),
    # diag
    pytest.param([1, 1], [2, 1], id='top-left-in'),
    pytest.param([6, 1], [6, 2], id='top-right-in'),
    pytest.param([6, 6], [5, 6], id='bottom-right-in'),
    pytest.param([1, 6], [1, 5], id='bottom-left-in'),
])
def test_rotate(p, expected):
    assert rotate(p) == expected
