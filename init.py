  import pytest
  from src.app import bar

  @pytest.fixture
  def lista_exemplo():
      return [1, 2, 3, 4]

  def test_bar_com_ fixture(lista_exemplo):
      assert bar(lista_exemplo) == sum(lista_exemplo)
