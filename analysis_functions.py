# Functions to find the minimum and maximum values in a list of numbers
#
# Input: numbers (list)
#
# Output: min (float), max (float)
#
def get_min_max(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        # Return None if the list is empty
        return None, None
    # Find the minimum and maximum values
    min_number = min(numbers)
    max_number = max(numbers)
    # Return the minimum and maximum values
    return min_number, max_number
