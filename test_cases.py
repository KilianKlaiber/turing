"""Test cases to demonstrate issues in the main.py code"""

from main import number_of_operations


def test_cases():
    print("Testing various cases to identify issues:")

    # Test case 1: Non-consecutive duplicates
    print(
        f"Test 1 - [1, 3, 1]: {number_of_operations([1, 3, 1])}"
    )  # Should be 1, but may be wrong

    # Test case 2: Multiple duplicates
    print(f"Test 2 - [1, 1, 1]: {number_of_operations([1, 1, 1])}")  # Should be 3

    # Test case 3: Numbers outside range
    print(f"Test 3 - [0, 5]: {number_of_operations([0, 5])}")  # Should be 5

    # Test case 4: Normal case
    print(f"Test 4 - [2, 1]: {number_of_operations([2, 1])}")  # Should be 0

    # Test case 5: Empty list
    print(f"Test 5 - []: {number_of_operations([])}")

    # Test case 6: Single element
    print(f"Test 6 - [5]: {number_of_operations([5])}")  # Should be 4


if __name__ == "__main__":
    test_cases()
