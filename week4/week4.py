# Exercise 2
def count_number_of_each(password):
    """
    Count the number of each type of character in a password: letters,
    digits, and special characters.

    Args:
        password (str): a password

    Returns (Tuple[int, int, int]): A tuple with the number of
        letters, digits, and special characters, in that order.
    """
    ### YOUR CODE GOES HERE

# Exercise 3
def compare(input, password, wildcards):
    """
    Compare a user's input to their actual password while accounting
    for a wildcard.

    Args:
        input (str): the user's input (the password the user entered)
        password (str): the user's actual password
        wildcards (List[str]): a list of one character wildcard strings

    Returns (int): The location of the first mismatch or -1 if the
        passwords match.
    """
    ### YOUR CODE GOES HERE


# Exercise 4
def compute_strength(password):
    """
    Compute the strength of a password. The strength of a password is
        computed using:
            +2 for each number
            +1 for each uppercase letter
            +2 for each special character
            +3 if it contains more than 8 characters

    Args:
        password (str): a password

    Returns (int): The strength of a password.
    """
    ### YOUR CODE GOES HERE


def create_password(phrase, strength):
    """
    Create a password from a phrase. If the resulting password is weak,
        add the special character "!" until is reaches a given strength.

    Args:
        phrase (str): a phrase
        strength (int): minimum strength of the created password

    Returns (str): the password created from the phrase
    """
    ### YOUR CODE GOES HERE
