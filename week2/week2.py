"""
CAPP 30121, Autumn 2026
Week #2 Practice Exercises
"""

# Exercise 1
# Add your solution for is_eisenstein_triple here.


# Exercise 2
def clamp_val(val, lb, ub):
    """
    Clamp val to the range [lb, ub].

    Args:
        val (int): the value to clamp
        lb (int): the lower bound of the range
        ub (int): the upper bound of the range

    Returns (int): the clampped value
    """
    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #3
def find_first_negative(lst):
    """
    Determine the first negative value in the list.

    Args:
        lst (List[int]): the list

    Returns (int): The first negative or zero.
    """
    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #4
def num_common_divisors(a, b):
    """
    Find the number of divisors a and b have in common.  You may
    assume that a <= b. For example, the common divisors of 12 and 18
    are 1, 2, 3 and 6, so the answer would be 4.

    Args:
        a (int): a positive integer
        b (int): a positive integer

    Returns (int): The number of common divisors of a and b.
    """
    # This assertion verifies that the value of a
    # is less than or equal to b.  It will halt the
    # computation and generate an AssertionError at runtime
    # if a > b.
    assert a <= b, "a must be less than or equal to b"

    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #5
def count_even_odd(lst):
    """
    Given a list of integers, produce a string: "EVEN", "ODD" or
    "NEITHER" depending on whether the list contains more even
    numbers, odd numbers or the same number of evens or odds.

    As a reminder, zero is an even number.

    Args:
        lst [List[int]]: a list of integers

    Returns (str): A string as described above.
    """
    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #6
def find_multiples(lst, x):
    """
    Given a list of integers, and an integer x, return a new list
    of numbers from the original list that are multiples of x.

    Args:
        lst (List[int]): the list of interest
        x (int): a positive integer

    Returns (List[int]): A list of the integers from the input
      list that are multiples of x.
    """
    assert x > 0

    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #7
def is_gray_scale(color):
    """
    Is color a gray-scale color?

    Args:
        color (Tuple[int, int, int]): the color of interest

    Returns (bool): True if the input color is a gray-scale
      color and False, otherwise.
    """
    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #8
def all_gray_scale(lst):
    """
    Are all the colors in the list gray-scale colors
    """

    ### Your code goes here.
    ### Replace None with a suitable return value
    return None


# Exercise #9
def clamp_lst_vals(lst, lb, ub):
    """
    Modify the input list so that all of the values are between lb and ub.

    Args:
        lst (list of floats): the list
        lb (float): the lower bound
        ub (float): the upper bound

    Modifies:
        lst - updates elements that are out-of-range

    Returns (None): Nothing
    """

    ### Your code goes here.
