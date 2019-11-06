from qnano.euler.sum_factors import sum_factors_less_than_z


def test_sum_factors_less_than_z():
    """Test sum_factors function."""
    assert sum_factors_less_than_z(3, 5, 10) == 23



