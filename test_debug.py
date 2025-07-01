from main import number_of_operations

# Test case to show the issue
test_input = [1, 1, 3]
print(f"Input: {test_input}")
print(f"Result: {number_of_operations(test_input)}")

# Let's trace through manually:
# Sorted input: [1, 1, 3]
# Length: 3
# Permutation: [1, 2, 3]
#
# Wrong numbers:
# - 3 is in permutation, so not added initially
# - 1 appears twice consecutively and 1 <= 3, so one 1 is added
# Wrong numbers: [1]
#
# Missing numbers:
# - 2 is not in [1, 1, 3], so 2 is missing
# Missing numbers: [2]
#
# Operations: |1 - 2| = 1
# Expected result: 1

# But what if we have a case where wrong_numbers could be empty?
test_input2 = [1, 2, 3]
print(f"\nInput: {test_input2}")
print(f"Result: {number_of_operations(test_input2)}")
