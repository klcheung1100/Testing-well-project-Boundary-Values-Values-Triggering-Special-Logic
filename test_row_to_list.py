# row_to_list() takes a row containing housing area and prices e.g. "2,041\t123,781\n" and returns the data as a list e.g. ["2,041", "123,781"]
# A row can be mapped to a 2-tuple (m, n), where m is the number of tab separators. n is 1 if the row has any missing values, and 0 otherwise.
# Example 1: "123\t456\n" ->  (1, 0).
# Example 2: "\t456\n" -> (1, 1).
# Example 3: "\t456\t\n" -> (2, 1).

# The function only returns a list for arguments mapping to (1, 0). All other tuples correspond to invalid rows, with either more than one tab or missing values. The function returns None in all these cases. (See the plot.svg)
# This mapping shows that the function has normal behavior at (1, 0), and special behavior everywhere else.

import pytest
from preprocessing_helpers import row_to_list

# Test row_to_list() with normal arguments i.e. arguments mapping to the tuple (1, 0).
def test_on_normal_argument_1():
    actual = row_to_list("123\t4,567\n")
    # Fill in with the expected return value for the argument "123\t4,567\n"
    expected = ["123", "4,567"]
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


def test_on_normal_argument_2():
    actual = row_to_list("1,059\t186,606\n")
    expected = ["1,059", "186,606"]
    # Write the assert statement along with a failure message
    assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


# Write test for boundary values
def test_on_no_tab_no_missing_value_boundary():  # (0, 0) boundary value
    # Assign actual to the return value for the argument "123\n"
    actual = row_to_list("123\n")
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_no_missing_value_boundary():  # (2, 0) boundary value
    actual = row_to_list("123\t4,567\t89\n")
    # Complete the assert statement
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


# write tests for values triggering special behavior, in particular, (0, 1) and (2, 1). These are values triggering special logic since the function returns None instead of a list.
def test_on_no_tab_with_missing_value():  # (0, 1) case
    # Assign to the actual return value for the argument "\n"
    actual = row_to_list("\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_with_missing_value():  # (2, 1) case
    # Assign to the actual return value for the argument "123\t\t89\n"
    actual = row_to_list("123\t\t89\n")
    # Write the assert statement with a failure message
    assert actual is None, "Expected: None, Actual: {0}".format(actual)
