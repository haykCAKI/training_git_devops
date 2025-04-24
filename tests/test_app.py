import pytest
from src.app import foo

def test_foo_valor_basico():
    assert foo(2) == 4
