# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the
# integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

def equal_sides(arr):

    if len(arr) == 1:
        return 0
    for i in range(len(arr)):


