import pytest
from src.app import foo

@pytest.mark.parametrize("input_, expected", [
      (0, 0),
      (-1, 1),
      (10, 100),
  ])
def test_foo_parametrizado(input_, expected):
    assert foo(input_) == expected

def test_foo_raises_type_error():
    with pytest.raises(TypeError):
        foo("texto")
