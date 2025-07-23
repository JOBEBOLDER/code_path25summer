'''
Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.


Understand:
    input: a sorted list of int and a int target
    Goal: go through the binary search list and return true if target is found, else: false
Plan:
    use binary search to go through the whole BST and return true if target is found
Implement:

'''

def find_cruise_length(cruise_lengths, vacation_length):
    # base case:
    if not cruise_lengths:
        return False
    left = 0
    right = len(cruise_lengths) - 1
    while left<= right:
        mid = (right-left) // 2 + left

        #if we find the target:
        if cruise_lengths[mid] == vacation_length:
            return True

        #the mid point digit is too small:
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        
        #the mid point digit is too large:
        elif cruise_lengths[mid] > vacation_length:
            right = mid - 1

    return False



print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))