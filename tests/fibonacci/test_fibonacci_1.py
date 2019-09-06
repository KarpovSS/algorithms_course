import pytest
from src.fibonacci.fibonacci_1 import fib


@pytest.mark.parametrize("n_input, n_output", [
    (1, 1),
    (2, 1),
    (3, 2),
    (8, 21)
])
def test_fib(n_input, n_output):
    assert fib(n_input) == n_output
