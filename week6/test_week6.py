import sys
import os
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import week6

MODULE = "week6"

# # #
#
# HELPER FUNCTIONS
#
# # #

def check_none(actual, recreate_msg=None):
    msg = "The method returned None."
    msg += " Did you forget a return statement?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if actual is None:
        return msg

    # test passed
    return None

def check_expected_none(actual, recreate_msg=None):
    msg = "The method is expected to return None."
    msg += " Your method returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if actual is not None:
        return msg

    # test passed
    return None

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The method returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if isinstance(actual, expected_type):
        return None
    else:
        return msg        

def check_attribute(actual, attribute_name, recreate_msg=None):
    msg = "Your class should have a '{}' attribute.".format(attribute_name)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if hasattr(actual, attribute_name):
        return None
    else:
        return msg

def check_attribute_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "Your class has an attribute of the wrong type.\n"
    msg += "  Expected type: {}.\n".format(expected_type.__name__)
    msg += "  Actual type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if isinstance(actual, expected_type):
        return None
    else:
        return msg

def check_equals(actual, expected, recreate_msg=None):
    msg = ("Actual ({}) and expected ({}) values " 
        "do not match.").format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if actual == expected:
        return None
    else:
        return msg

def check_float_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if abs(actual-expected) < 0.01:
        return None
    else:
        return msg

def check_parameter_unmodified(actual, expected, param, recreate_msg=None):
    msg = ("Parameter {} has been modified:\n"
        "Actual ({}) and original ({}) values of {}" 
        "do not match.").format(param, param, actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    if actual == expected:
        return None
    else:
        return msg

def pretty_print_repr(x):
    return repr(x)

def gen_recreate_msg(module, function, *params, **kwparams):
    params_str = ", ".join([pretty_print_repr(p) for p in params])
    if len(kwparams) > 0:
        params_str += ", ".join(["{} = {}".format(k, repr(v)) 
            for k, v in kwparams.items()])
    lines = ["{}.{}({})".format(module, function, params_str)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_by_lines(lines):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  " + "\n  ".join(lines)
    return recreate_msg

# # #
#
# TESTS
#
# # #

def do_test_sum_of_powers(p, N, expected):
    recreate_msg = gen_recreate_msg(MODULE, "sum_of_powers", (p, N))
    actual = week6.sum_of_powers(p, N)
    err_msg1 = check_none(actual, recreate_msg)
    if err_msg1:
        return err_msg1
    err_msg2 = check_type(actual, expected, recreate_msg)
    if err_msg2:
        return err_msg2
    err_msg3 = check_equals(actual, expected, recreate_msg)
    if err_msg3:
        return err_msg3

def do_test_value_of(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "value_of", lst)
    actual = week6.value_of(lst)
    err_msg1 = check_none(actual, recreate_msg)
    if err_msg1:
        return err_msg1
    err_msg2 = check_type(actual, expected, recreate_msg)
    if err_msg2:
        return err_msg2
    err_msg3 = check_equals(actual, expected, recreate_msg)
    if err_msg3:
        return err_msg3

def do_test_index_of(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "index_of", lst)
    actual = week6.index_of(lst)
    err_msg1 = check_none(actual, recreate_msg)
    if err_msg1:
        return err_msg1
    err_msg2 = check_type(actual, expected, recreate_msg)
    if err_msg2:
        return err_msg2
    err_msg3 = check_equals(actual, expected, recreate_msg)
    if err_msg3:
        return err_msg3

# # #
#
# TEST HELPERS
#
# # #

# SUM OF POWERS
def calculate_solution(p, N):
    sum = 0
    for i in range(N+1):
        sum += p**i
    return sum

def test_sum_of_powers_1():
    p = 2
    N = 2
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_2():
    p = 1
    N = 2
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_3():
    p = 2
    N = 1
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_4():
    p = 2
    N = 3
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_5():
    p = 2
    N = 5
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_6():
    p = 2
    N = 7
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_7():
    p = 4
    N = 3
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_sum_of_powers_8():
    p = 6
    N = 3
    err_msg = do_test_sum_of_powers(p, N, calculate_solution(p, N))
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

# VALUE OF FIRST NEGATIVE
def test_value_of_1():
    lst = [-1]
    err_msg = do_test_value_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_2():
    lst = [-1, 2, 3, 4]
    err_msg = do_test_value_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_3():
    lst = [1, -2, 3, 4]
    err_msg = do_test_value_of(lst, -2)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_4():
    lst = [1, 2, 3, -4]
    err_msg = do_test_value_of(lst, -4)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_5():
    lst = [-1, 2, 3, -4]
    err_msg = do_test_value_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_6():
    lst = [1, -2, 3, -4]
    err_msg = do_test_value_of(lst, -2)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_7():
    lst = [-1, -2, -3, -4]
    err_msg = do_test_value_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_8():
    lst = [1, 2, 3, 4]
    err_msg = do_test_value_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_9():
    lst = [1]
    err_msg = do_test_value_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_value_of_10():
    lst = []
    err_msg = do_test_value_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

# INDEX OF FIRST NEGATIVE
def test_index_of_1():
    lst = [-1]
    err_msg = do_test_index_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_2():
    lst = [-1, 2, 3, 4]
    err_msg = do_test_index_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_3():
    lst = [1, -2, 3, 4]
    err_msg = do_test_index_of(lst, 1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_4():
    lst = [1, 2, 3, -4]
    err_msg = do_test_index_of(lst, 3)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_5():
    lst = [-1, 2, 3, -4]
    err_msg = do_test_index_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_6():
    lst = [1, -2, 3, -4]
    err_msg = do_test_index_of(lst, 1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_7():
    lst = [-1, -2, -3, -4]
    err_msg = do_test_index_of(lst, 0)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_8():
    lst = [1, 2, 3, 4]
    err_msg = do_test_index_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_9():
    lst = [1]
    err_msg = do_test_index_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

def test_index_of_10():
    lst = []
    err_msg = do_test_index_of(lst, -1)
    if err_msg:
        pytest.fail(err_msg)
    # test passed
    return None

