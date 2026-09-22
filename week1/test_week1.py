import week1
import sys
import os
import helpers
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())


MODULE = "week1"


@pytest.mark.parametrize("a,x,expected", [(2, 3, 64), (3, 2, 25),
                                          (4, 0, 1), (0, 4, 16)])
def test_add_two_and_raise(a, x, expected):
    """Test add_two_and_raise"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_two_and_raise", a, x)

    try:
        actual = week1.add_two_and_raise(a, x)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("p,r,n,expected", [
    (100, 0.05, 2, 110.25),
    (200, 0.1, 3, 266.2),
    (50, 0.2, 5, 124.416)])
def test_compound_loan_amount(p, r, n, expected):
    """Test compound_loan_amount"""
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "compound_loan_amount", p, r, n)

    try:
        actual = week1.compound_loan_amount(p, r, n)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a,b,expected", [(2, 3, False), (3, -2, True),
                                          (-4, -1, False), (-10, 4, True)])
def test_different_sign(a, b, expected):
    """Test different_sign"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "same_sign", a, b)

    try:
        actual = week1.different_sign(a, b)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

