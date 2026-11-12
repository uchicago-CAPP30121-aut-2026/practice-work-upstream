import sys
import os
import pytest

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import week7
import util
from tree import Tree

MODULE = "week7"

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
    msg = ("Actual ({}) and expected ({}) values do not match.").format(
        actual, expected
    )
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

    if abs(actual - expected) < 0.01:
        return None
    else:
        return msg


def check_parameter_unmodified(actual, expected, param, recreate_msg=None):
    msg = (
        "Parameter {} has been modified:\n"
        "Actual ({}) and original ({}) values of {}"
        "do not match."
    ).format(param, param, actual, expected)
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
        params_str += ", ".join(
            ["{} = {}".format(k, repr(v)) for k, v in kwparams.items()]
        )
    lines = ["{}.{}({})".format(module, function, params_str)]
    return gen_recreate_msg_by_lines(lines)


def gen_recreate_msg_by_lines(lines):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  " + "\n  ".join(lines)
    return recreate_msg


def gen_recreate_msg_with_trees(module, function, tree_name, *params):
    params_str = "".join([", " + pretty_print_repr(p) for p in params])
    lines = [
        "import util",
        'trees = util.load_trees("sample_trees.json")',
        '{}.{}(trees["{}"]{})'.format(module, function, tree_name, params_str),
    ]
    return gen_recreate_msg_by_lines(lines)


def check_tree_equals(t, expected_t, recreate_msg):
    check_tree_helper(
        t, expected_t, "Actual and expected values do not match:", recreate_msg
    )


def check_tree_unmodified(t, expected_t, recreate_msg):
    check_tree_helper(t, expected_t, "Tree has been modified:", recreate_msg)


def check_tree_helper(t, expected_t, top_msg, recreate_msg):
    expected_attributes = vars(expected_t)

    node_error_prefix = (
        "Checking a node with "
        + ", ".join(
            [
                "{}={}".format(attr, repr(getattr(t, attr, "[not assigned]")))
                for attr in expected_attributes
                if attr != "children"
            ]
        )
        + "\n{}\n".format(top_msg)
    )

    for attr in expected_attributes:
        if not hasattr(t, attr):
            return (
                node_error_prefix
                + "Node is missing attribute {}.\n".format(attr)
                + recreate_msg
            )

        if attr != "children":
            if getattr(t, attr) != getattr(expected_t, attr):
                return (
                    node_error_prefix + "Node has incorrect {}. Got {}, expected {}.\n"
                ).format(
                    attr, repr(getattr(t, attr)), repr(getattr(expected_t, attr))
                ) + recreate_msg

    expected_attributes_set = set(expected_attributes.keys())
    actual_attributes_set = set(vars(t).keys())
    if actual_attributes_set != expected_attributes_set:
        return (
            node_error_prefix
            + "Node has extra attributes {}.\n".format(
                ", ".join(actual_attributes_set - expected_attributes_set)
            )
            + recreate_msg
        )

    children = list(t.children)
    expected_children = list(expected_t.children)

    if expected_children == []:
        if children != []:
            return (
                node_error_prefix
                + "Expected node to have no children, but it has children.\n"
                + recreate_msg
            )
    else:
        for c in children:
            if not isinstance(c, Tree):
                return (
                    node_error_prefix
                    + "Node has a child that is not a Tree: {}\n".format(c)
                    + recreate_msg
                )

        # This assumes no node has two children with the same key
        sorted_children = sorted(children, key=lambda st: st.key)
        sorted_expected_children = sorted(expected_children, key=lambda st: st.key)
        keys = [c.key for c in sorted_children]
        expected_keys = [c.key for c in sorted_expected_children]

        if keys != expected_keys:
            return (
                node_error_prefix
                + "Expected node to have children with keys {} "
                "but the children's keys are {}.\n".format(expected_keys, keys)
                + recreate_msg
            )

        for child, expected_child in zip(sorted_children, sorted_expected_children):
            err_msg = check_tree_helper(child, expected_child, top_msg, recreate_msg)
            if err_msg:
                return err_msg

        # test passed!
        return None


# # #
#
# TEST HELPERS
#
# # #


def copy_tree(tree):
    print(tree.key, tree.value)
    new_tree = Tree(tree.key, tree.value)
    for kid in tree.children:
        new_tree.add_child(copy_tree(kid))
    return new_tree


def do_test_find_min_max(tree, tree_name, expected):
    original_tree = copy_tree(tree)
    recreate_msg = gen_recreate_msg_with_trees(MODULE, "min_depth_leaf", tree_name)
    actual = week7.find_min_max(tree)

    err_msg = check_none(actual, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_type(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_equals(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_tree_unmodified(tree, original_tree, recreate_msg)
    if err_msg:
        return err_msg

    # test passed
    return None


def do_test_min_depth_leaf(tree, tree_name, expected):
    original_tree = copy_tree(tree)
    recreate_msg = gen_recreate_msg_with_trees(MODULE, "min_depth_leaf", tree_name)
    actual = week7.min_depth_leaf(tree)

    err_msg = check_none(actual, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_type(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_equals(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_tree_unmodified(tree, original_tree, recreate_msg)
    if err_msg:
        return err_msg

    # test passed
    return None


def do_test_has_increasing_values(tree, test_num, expected):
    original_tree = copy_tree(tree)
    recreate_msg = "See test_week7.py, increasing_values test {} for tree".format(
        test_num
    )
    actual = week7.has_increasing_values(tree)
    err_msg = check_none(actual, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_type(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_equals(actual, expected, recreate_msg)
    if err_msg:
        return err_msg

    err_msg = check_tree_unmodified(tree, original_tree, recreate_msg)
    if err_msg:
        return err_msg

    # test passed
    return None


# # #
#
# TESTS
#
# # #


# FIND_MIN_MAX
# Test 1:
def test_find_min_max_1():
    a = Tree("A", 10)
    b = Tree("B", 20)
    tree = a
    a.add_child(b)
    err_msg = do_test_find_min_max(tree, "1", (10, 20))
    if err_msg:
        pytest.fail(err_msg)


# Test 2:
def test_find_min_max_2():
    a = Tree("A", 10)
    b = Tree("B", 20)
    c = Tree("C", 70)
    tree = a
    a.add_child(b)
    a.add_child(c)
    err_msg = do_test_find_min_max(tree, "2", (10, 70))
    if err_msg:
        pytest.fail(err_msg)


# Test 3:
def test_find_min_max_3():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    tree = c
    c.add_child(f)
    f.add_child(g)
    err_msg = do_test_find_min_max(tree, "3", (70, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 4:
def test_find_min_max_4():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    j = Tree("J", 90)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(j)
    err_msg = do_test_find_min_max(tree, "4", (70, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 5:
def test_find_min_max_5():
    c = Tree("C", 70)
    g = Tree("G", 120)
    h = Tree("H", 40)
    f = Tree("F", 80)
    k = Tree("K", 100)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(h)
    err_msg = do_test_find_min_max(tree, "5", (40, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 6:
def test_find_min_max_6():
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    err_msg = do_test_find_min_max(tree, "6", (70, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 7:
def test_find_min_max_7():
    a = Tree("A", 10)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    err_msg = do_test_find_min_max(tree, "7", (10, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 8:
def test_find_min_max_8():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 5)
    tree = c
    c.add_child(f)
    c.add_child(k)
    c.add_child(b)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    err_msg = do_test_find_min_max(tree, "8", (5, 120))
    if err_msg:
        pytest.fail(err_msg)


# Test 9:
def test_find_min_max_9():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    f = Tree("F", 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    a.add_child(b)
    err_msg = do_test_find_min_max(tree, "9", (10, 80))
    if err_msg:
        pytest.fail(err_msg)


# Test 10:
def test_find_min_max_10():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    f.add_child(g)
    a.add_child(b)
    err_msg = do_test_find_min_max(tree, "10", (10, 120))
    if err_msg:
        pytest.fail(err_msg)


# MIN DEPTH OF A LEAF
# Test 1:
def test_min_depth_leaf_1():
    a = Tree("A", 10)
    b = Tree("B", 20)
    tree = a
    a.add_child(b)
    err_msg = do_test_min_depth_leaf(tree, "1", 1)
    if err_msg:
        pytest.fail(err_msg)


# Test 2:
def test_min_depth_leaf_2():
    a = Tree("A", 10)
    b = Tree("B", 20)
    c = Tree("C", 70)
    tree = a
    a.add_child(b)
    a.add_child(c)
    err_msg = do_test_min_depth_leaf(tree, "2", 1)
    if err_msg:
        pytest.fail(err_msg)


# Test 3:
def test_min_depth_leaf_3():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    tree = c
    c.add_child(f)
    f.add_child(g)
    err_msg = do_test_min_depth_leaf(tree, "3", 2)
    if err_msg:
        pytest.fail(err_msg)


# Test 4:
def test_min_depth_leaf_4():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    j = Tree("J", 90)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(j)
    err_msg = do_test_min_depth_leaf(tree, "4", 2)
    if err_msg:
        pytest.fail(err_msg)


# Test 5:
def test_min_depth_leaf_5():
    c = Tree("C", 70)
    g = Tree("G", 120)
    h = Tree("H", 40)
    f = Tree("F", 80)
    k = Tree("K", 100)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(h)
    err_msg = do_test_min_depth_leaf(tree, "5", 1)
    if err_msg:
        pytest.fail(err_msg)


# Test 6:
def test_min_depth_leaf_6():
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    err_msg = do_test_min_depth_leaf(tree, "6", 2)
    if err_msg:
        pytest.fail(err_msg)


# Test 7:
def test_min_depth_leaf_7():
    a = Tree("A", 10)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    err_msg = do_test_min_depth_leaf(tree, "7", 2)
    if err_msg:
        pytest.fail(err_msg)


# Test 8:
def test_min_depth_leaf_8():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 5)
    tree = c
    c.add_child(f)
    c.add_child(k)
    c.add_child(b)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    g.add_child(a)
    err_msg = do_test_min_depth_leaf(tree, "8", 1)
    if err_msg:
        pytest.fail(err_msg)


# Test 9:
def test_min_depth_leaf_9():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    f = Tree("F", 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    a.add_child(b)
    err_msg = do_test_min_depth_leaf(tree, "9", 3)
    if err_msg:
        pytest.fail(err_msg)


# Test 10:
def test_min_depth_leaf_10():
    a = Tree("A", 10)
    b = Tree("B", 70)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    tree = c
    c.add_child(f)
    f.add_child(a)
    f.add_child(g)
    a.add_child(b)
    err_msg = do_test_min_depth_leaf(tree, "10", 2)
    if err_msg:
        pytest.fail(err_msg)


# INCREASING VALUES
# Test 1:
def test_has_increasing_values_1():
    a = Tree("A", 10)
    tree = a
    err_msg = do_test_has_increasing_values(tree, "1", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 2:
def test_has_increasing_values_2():
    a = Tree("A", 10)
    b = Tree("B", 20)
    tree = a
    a.add_child(b)
    err_msg = do_test_has_increasing_values(tree, "2", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 3:
def test_has_increasing_values_3():
    a = Tree("A", 10)
    b = Tree("B", 20)
    c = Tree("C", 70)
    tree = a
    a.add_child(b)
    a.add_child(c)
    err_msg = do_test_has_increasing_values(tree, "3", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 4:
def test_has_increasing_values_4():
    b = Tree("B", 20)
    c = Tree("C", 70)
    f = Tree("F", 80)
    tree = f
    f.add_child(b)
    f.add_child(c)
    err_msg = do_test_has_increasing_values(tree, "4", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 5:
def test_has_increasing_values_5():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    tree = f
    f.add_child(g)
    f.add_child(c)
    err_msg = do_test_has_increasing_values(tree, "5", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 6:
def test_has_increasing_values_6():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    tree = f
    f.add_child(c)
    f.add_child(g)
    err_msg = do_test_has_increasing_values(tree, "6", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 7:
def test_has_increasing_values_7():
    c = Tree("C", 70)
    f = Tree("F", 80)
    tree = f
    f.add_child(c)
    err_msg = do_test_has_increasing_values(tree, "7", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 8:
def test_has_increasing_values_8():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    tree = c
    c.add_child(f)
    f.add_child(g)
    err_msg = do_test_has_increasing_values(tree, "8", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 9:
def test_has_increasing_values_9():
    c = Tree("C", 70)
    f = Tree("F", 80)
    g = Tree("G", 120)
    j = Tree("J", 90)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(j)
    err_msg = do_test_has_increasing_values(tree, "9", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 10:
def test_has_increasing_values_10():
    c = Tree("C", 70)
    g = Tree("G", 120)
    h = Tree("H", 40)
    f = Tree("F", 80)
    tree = c
    c.add_child(f)
    f.add_child(g)
    f.add_child(h)
    err_msg = do_test_has_increasing_values(tree, "10", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 11:
def test_has_increasing_values_11():
    c = Tree("C", 70)
    g = Tree("G", 120)
    h = Tree("H", 40)
    f = Tree("F", 80)
    k = Tree("K", 100)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(h)
    err_msg = do_test_has_increasing_values(tree, "11", False)
    if err_msg:
        pytest.fail(err_msg)


# Test 12:
def test_has_increasing_values_12():
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    f.add_child(g)
    f.add_child(l)
    err_msg = do_test_has_increasing_values(tree, "12", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 13:
def test_has_increasing_values_13():
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(l)
    f.add_child(g)
    f.add_child(l)
    err_msg = do_test_has_increasing_values(tree, "13", True)
    if err_msg:
        pytest.fail(err_msg)


# Test 14:
def test_has_increasing_values_14():
    a = Tree("A", 10)
    c = Tree("C", 70)
    g = Tree("G", 120)
    f = Tree("F", 80)
    k = Tree("K", 100)
    l = Tree("L", 110)
    tree = c
    c.add_child(f)
    c.add_child(k)
    k.add_child(a)
    f.add_child(g)
    f.add_child(l)
    err_msg = do_test_has_increasing_values(tree, "14", False)
    if err_msg:
        pytest.fail(err_msg)
