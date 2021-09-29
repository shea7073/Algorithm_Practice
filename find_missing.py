# find the missing #

def finder(arr1, arr2):
    log = {}
    for num in arr1:
        log[num] = arr1.count(num)
    print(log)
    for num in arr2:
        if num in log.keys():
            log[num] -= 1
    print(log)
    for num in log:
        if log[num] > 0:
            for i in range(0, log[num]):
                print(num)


finder([1, 2, 3, 3, 5, 5, 6], [3, 6, 2, 5])