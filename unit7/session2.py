def find_cruise_length(cruise_lengths, vacation_length):
    #base case:
    if not cruise_lengths:
        return False
    
    #binary search
    left = 0
    right = len(cruise_lengths) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if vacation_length == cruise_lengths[mid]:
            return True
        
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1

    return False



print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


def find_cabin_index(cabins, preferred_deck):
    if not cabins:
        return 0
    
    left = 0
    right = len(cabins) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] < preferred_deck:
            left = mid +  1

        elif cabins[mid] > preferred_deck:
            right  = mid - 1

    return left  # Return the index where the preferred deck can be inserted
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

def count_checked_in_passengers(rooms):
    #base case:
    if not rooms:
        return None
    
    left = 0
    right = len(rooms) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if rooms[mid] == 0:
            left = mid + 1

        else:
            right = mid - 1

    return len(rooms) - left
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]
print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))


def is_profitable(excursion_counts):
    # first sort the list to apply binary search
    excursion_counts.sort()
    n = len(excursion_counts)

    # start from the end
    for i in range(n):
        x = n - i  #it means right now how many people behind 

        #when count to the i digit, and this one is larger than x,then we can consider to keep counting moving forward 
        if excursion_counts[i] >= x:
            #the condition will end when we find the previous one is smaller than x,then we find -----(smaller)x ------(larger)
            if i == 0 or excursion_counts[i - 1] < x:
                return x  # 找到了唯一满足的 x

    return -1  # can not find it


def find_shallowest_point(arr):
    if not arr:
        return None
    
    #recrusive stop condition
    if len(arr) == 2:
        return arr[0]
    
    mid = len(arr) // 2
    left_min = find_shallowest_point(arr[:mid])
    right_min = find_shallowest_point(arr[mid:])

    return left_min if left_min < right_min else right_min

print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))