"""
Permutation = List of distinct positive numbers from 1 to N

Operation: Incrementing or decrementing a number by 1

Challenge: Detect the number of operations for turning a list of numbers into a permutation

IV. Check edge cases
"""

def number_of_operations(list_of_numbers: list[int]) -> int | str:
    
    """ Return the number of steps necessary for turing the list into a permutation"""
    
    list_of_numbers = sorted(list_of_numbers)
    length = len(list_of_numbers)
    
    if length == 0:
        return 'List of numbers must be non empty'

    # Create a list of the final permutation
    permutation = list(range(1,length+1))
    
    # find wrong numbers missing in the list of numbers
    wrong_numbers = []
    for number in list_of_numbers:
        if number not in permutation:
            wrong_numbers.append(number)
    
    # Identify duplicates and add them to the list of wrong numbers
    
    for index, number in enumerate(list_of_numbers):
        if index < length - 1:
            if number == list_of_numbers[index + 1]:
                wrong_numbers.append(number)
    
    # Identify missing numbers in the list of numbers
    
    missing_numbers = []
    
    for number in permutation:
        if number not in list_of_numbers:
            missing_numbers.append(number)
    
    # For each missing number
    operation_number = 0
    for missing_number in missing_numbers:
        #Find wrong number closest to missing number
        
        closest_number = wrong_numbers[0]
        
        for wrong_number in wrong_numbers:
            if abs(wrong_number-missing_number) < abs(wrong_number - closest_number):
                closest_number = wrong_number
        # Calculate the distance to the missing number and add it to the minimum number of operations
        operation_number += abs(closest_number - missing_number)
        # Delete the closest wrong number for the list of wrong numbers
        wrong_numbers.remove(closest_number)
    
    return operation_number
          


if __name__ == "__main__":
    result = number_of_operations([7,5])
    
    print(result)
