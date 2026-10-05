import sys
import os
import helpers
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import week2

MODULE = "week2"


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 8, 7, True),
        (5, 8, 7, True),
        (5, 21, 19, True),
        (3, 9, 7, False),
        (4, 8, 7, False),
        (3, 8, 6, False),
    ],
)
def test_eisenstein_triple(a, b, c, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "eisenstein_triple", *(a, b, c))
    try:
        actual = week2.is_eisenstein_triple(a, b, c)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


clamp_tests = [
    (15, 10, 20, 15),
    (10, 10, 20, 10),
    (0, 10, 20, 10),
    (25, 10, 20, 20),
    (-10, 0, 100, 0),
    (200, 0, 100, 100),
    (99, 0, 100, 99),
]


@pytest.mark.parametrize("val,lb,ub,expected", clamp_tests)
def test_clamp_val(val, lb, ub, expected):
    """
    Test the conditional version of clamp
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "clamp_val", val, lb, ub)

    try:
        actual = week2.clamp_val(val, lb, ub)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([-1, 0], -1),
        ([0, -1], -1),
        ([0, -1, -3], -1),
        ([0, 1, -3, 2], -3),
        ([0, 1, 3, 2, 4, -5], -5),
        ([0, 1, 3, 2, 4, 5], 0),
        ([], 0),
        ([-1], -1),
    ],
)
def test_find_first_negative(lst, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "first_negative", *(lst,))

    orig = lst[:]
    try:
        actual = week2.find_first_negative(lst)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_type(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))
    err_msgs.append(helpers.check_list_unmodified("lst", orig, lst))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a,b,expected", [(12, 18, 4), (3, 5, 1), (4, 4, 3), (1, 1, 1)])
def test_num_common_divisors(a, b, expected):
    """Test num_common_divisors"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "num_common_divisors", a, b)

    try:
        actual = week2.num_common_divisors(a, b)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 2, 3, 4, 5], "ODD"),
        ([1, 2, 3, 4, 5, 6], "NEITHER"),
        ([1, 2, 3, 4, 5, 6, 7], "ODD"),
        ([1, 2, 3, 4, 5, 6, 7, 8], "NEITHER"),
        ([0, 2, 4], "EVEN"),
        ([0, 1, 3], "ODD"),
        ([0], "EVEN"),
        ([], "NEITHER"),
    ],
)
def test_count_even_odd(lst, expected):
    """Test count_even_odd"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_even_odd", lst)

    lst_copy = lst.copy()

    try:
        actual = week2.count_even_odd(lst)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # Check that the original list was not modified
    err_msg = helpers.check_list_unmodified("lst", lst, lst_copy)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize(
    "lst,x,expected",
    [
        ([], 2, []),
        ([3], 3, [3]),
        ([10], 3, []),
        ([1, 2, 3, 4, 5, 6], 2, [2, 4, 6]),
        ([1, 2, 3, 4, 5, 6], 3, [3, 6]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [5, 10]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ],
)
def test_find_multiples(lst, x, expected):
    """Test find_multiples"""
    recreate_msg = helpers.gen_recreate_msg(MODULE, "keep_if_multiple", lst, x)

    lst_copy = lst.copy()

    try:
        actual = week2.find_multiples(lst, x)
    except Exception as e:  # pylint: disable=broad-except
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # Check that the original list was not modified
    err_msg = helpers.check_list_unmodified("lst", lst, lst_copy)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize(
    "color, expected",
    [
        ((0, 0, 0), True),
        ((255, 255, 255), True),
        ((128, 128, 128), True),
        ((126, 127, 128), False),
        ((0, 0, 255), False),
        ((0, 128, 0), False),
        ((17, 17, 0), False),
    ],
)
def test_is_gray_scale(color, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_gray_scale", color)

    try:
        actual = week2.is_gray_scale(color)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([(0, 0, 0)], True),
        ([(126, 127, 128)], False),
        ([], True),
        ([(0, 0, 0), (255, 255, 255), (10, 10, 10)], True),
        ([(0, 0, 0), (0, 255, 255), (10, 10, 10)], False),
    ],
)
def test_all_gray_scale(lst, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "all_gray_scale", lst)

    try:
        actual = week2.all_gray_scale(lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, expected))
    err_msgs.append(helpers.check_equals(actual, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize(
    "lst, lb, ub, expected",
    [
        ([], 0, 2, []),
        ([1], 0, 2, [1]),
        ([0, 1, 2], 0, 2, [0, 1, 2]),
        ([1, 4, 4, 3, -3], -2, 5, [1, 4, 4, 3, -2]),
        ([-1, 9, 0, 3, 3, 7], -2, 5, [-1, 5, 0, 3, 3, 5]),
        ([0, -1, 2, 4, -5, 7, 1], 0, 2, [0, 0, 2, 2, 0, 2, 1]),
    ],
)
def test_clamp_lst_vals(lst, lb, ub, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "clamp_lst_vals", *(lst, lb, ub))

    lst_copy = lst[:]
    try:
        actual = week2.clamp_lst_vals(lst_copy, lb, ub)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msgs = []
    err_msgs.append(helpers.check_none(actual, None))
    err_msgs.append(helpers.check_equals(lst_copy, expected))

    for err_msg in err_msgs:
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)
