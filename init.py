  from src.app import bar, baz

  def test_bar_comportamento():
      assert bar([1, 2, 3]) == 6

  def test_baz_vazio():
      assert baz([]) is None
