
def shuffle():
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    numsx = nums[0:3]
    numsy = nums[3:]
    final = []
    print(numsx)
    print(numsy)

    for i in range(0, n):
        final.append(numsx[i])
        final.append(numsy[i])

    print(final)
    return final


shuffle()
