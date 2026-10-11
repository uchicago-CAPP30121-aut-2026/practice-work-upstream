"""
CAPP 30121, Autumn 2026
Week #2 Practice Exercises
"""


# Exercise 2
def count_val_types(matrix):
    """
    Count the number of number of values the input matrix that are
    less than zero, equal zero, and are greater than zero.

    Args:
        matrix (List[List[int]]): the input matrix

    Returns (Tuple(int, int, int)): a tuple with the number
    of values in the input matrix that are less than zero,
    equal to zero, and greater than zero.
    """

    # Your code goes here


def test_count_val_types():
    """
    A few tests for count_val_types
    """

    # From writeup: more columns than rows
    m1 = [[2.3, -1.2, 5.4, 8.8], [-9.9, 0.0, 10.0, -0.1], [2.4, -5.7, 8.9, 3.3]]
    assert count_val_types(m1) == (4, 1, 7)

    # More rows than columns
    m2 = [
        [2.3, -1.2, 5.4, 8.8],
        [-9.9, 0.0, 10.0, -0.1],
        [2.4, -5.7, 8.9, 3.3],
        [1.1, 2.2, 4.4, 5.5],
        [-1.1, -2.2, -4.4, -25.5],
    ]
    assert count_val_types(m2) == (8, 1, 11)

    # degenerate case
    m3 = [[0]]
    assert count_val_types(m3) == (0, 1, 0)


# Exercise 4
def word_length(lst):
    """
    Given a list of strings, compute a dictionary that
    maps each string to its length.

    Args:
        lst (List[str]): a list of strings

    Returns (Dict[str, int]): a dictionary that maps
      each (unique) string to its length
    """
    # Your code goes here


def test_word_length():
    """
    A few tests for word_length
    """
    # example from the writeup
    lst1 = ["hello", "goodbye", "bye"]
    word_length(lst1) == {"hello": 5, "goodbye": 7, "bye": 3}

    # example used in question in the writeup
    lst2 = ["hello", "hello", "goodbye", "bye", "hola", "hello"]
    word_length(lst2) == {"hello": 5, "goodbye": 7, "bye": 3, "hola": 4}


# Exercise 5
def words_start_with(lst):
    """
    Given a list of (non-empty) words, that takes a list of
    (non-empty) words (strings) as input.  The function computes a
    dictionary that maps the first letter of each word to the number
    of words in the list that start with that letter.

    Args:
        lst (List[str]): a list of strings

    Returns (Dict[str, int]): a dictionary that maps
      a letter to the number of words in the list
      that start with that letter.
    """
    # Your code goes here


def test_words_start_with():
    """
    A few tests for words_start_with
    """

    # Your code goes here

    # simple case to start
    ex1 = words_start_with(["hi"])
    assert ex1 == {"h": 1}

    # from the writeup
    ex2 = words_start_with(["hi", "bye", "ape", "book", "apple", "ant"])
    assert ex2 == {"h": 1, "b": 2, "a": 3}

    # degenerate case
    assert words_start_with([]) == {}


# Exercise 6
def find_state_with_max(state_to_num_complaints):
    """
    Given a dictionary that maps state abbreviations
    to the number of complaints from that state, find
    the state with the fewest complaints.  Break ties
    by returning the state with the abbreviation
    that comes earlier in dictionary ordering.

    Args:
        state_to_num_complaints (Dict[str, int]): a dictionary
          that maps state abbreviations to the number of complaints
          from that state.

    Returns (str | None): the name of the state with the
      most complaints or None, if the input dictionary
      is empty.
    """

    # Your code goes here


def test_find_state_with_max():
    """
    A few tests for find_state_with_max
    """

    # No ties
    assert find_state_with_max({"NJ": 20, "AZ": 10}) == "NJ"

    # from writeup
    state_to_num_complaints = {"AZ": 10, "AL": 10, "IL": 20, "NJ": 20, "WA": 5}
    assert find_state_with_max(state_to_num_complaints) == "IL"

    # degenerate case
    assert find_state_with_max({}) is None


# Exercise 7
def complaints_by_company(complaints):
    """
    Create a dictionary that maps the name of a company to a list of the
    complaint dictionaries that concern that company.

    Args:
        complaints (List[Dict[str, str]]) A list of complaints,
           where each complaint is a dictionary

    Returns: (Dict[str, List[Dict[str, str]]) mapping the name of the company
      to a list of complaints about that company.
    """
    # Your code goes here


def test_complaints_by_company():
    """
    A few tests for find_state_with_max
    """
    # from writeup
    sample_cfpb = [
        {"Company": "Discover", "State": "MN"},
        {"Company": "Bank of Hawaii", "State": "HI"},
        {"Company": "Synchrony Financial", "State": "NY"},
        {"Company": "Capital One", "State": "NY"},
        {"Company": "Capital One", "State": "MA"},
        {"Company": "Ocwen", "State": "HI"},
        {"Company": "Capital One", "State": "FL"},
        {"Company": "Capital One", "State": "OK"},
        {"Company": "PNC Bank N.A.", "State": "NC"},
        {"Company": "Capital One", "State": "WA"},
    ]

    # test just the first complain
    expected1 = {"Discover": [sample_cfpb[0]]}
    assert complaints_by_company(sample_cfpb[:1]) == expected1

    # test one company with multiple complaints
    lst = [sample_cfpb[3], sample_cfpb[4], sample_cfpb[6]]
    expected2 = {
        "Capital One": [
            {"Company": "Capital One", "State": "NY"},
            {"Company": "Capital One", "State": "MA"},
            {"Company": "Capital One", "State": "FL"},
        ]
    }

    assert complaints_by_company(lst) == expected2

    # Example from writeup
    expected3 = {
        "Discover": [{"Company": "Discover", "State": "MN"}],
        "Bank of Hawaii": [{"Company": "Bank of Hawaii", "State": "HI"}],
        "Synchrony Financial": [{"Company": "Synchrony Financial", "State": "NY"}],
        "Capital One": [
            {"Company": "Capital One", "State": "NY"},
            {"Company": "Capital One", "State": "MA"},
            {"Company": "Capital One", "State": "FL"},
            {"Company": "Capital One", "State": "OK"},
            {"Company": "Capital One", "State": "WA"},
        ],
        "Ocwen": [{"Company": "Ocwen", "State": "HI"}],
        "PNC Bank N.A.": [{"Company": "PNC Bank N.A.", "State": "NC"}],
    }
    assert complaints_by_company(sample_cfpb) == expected3


if __name__ == "__main__":
    test_count_val_types()
    test_word_length()
    test_words_start_with()
    test_find_state_with_max()
    test_complaints_by_company()
