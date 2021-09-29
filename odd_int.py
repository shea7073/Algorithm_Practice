# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def odd_int(arr):
    if len(arr) == 1:
        return arr[0]
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for key in counts:
        if counts[key] % 2 == 1:
            return key


print(odd_int([1, 2, 2, 3, 3]))
