import pytest

from task2 import calculate


def test_input_params():
    with pytest.raises(TypeError):
        calculate('3', 3, [10, 4, 8])
    with pytest.raises(TypeError):
        calculate(3, 3, ['10', 4, 8])


@pytest.mark.parametrize('m, n, p, r', [(3, 3, [6, 2, 3], 12),
                                        (3, 3, [10, 4, 8], 22),
                                        (3, 3, [2, 4, 8], 14)])
def test_accuracy(m, n, p, r):
    assert calculate(m, n, p) == r
