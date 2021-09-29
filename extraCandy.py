def extracandy(candies, extracandies):
    highest = 0
    returns = []
    for element in candies:
        if element > highest:
            highest = element

    for element in candies:
        if element + extracandies >= highest:
            returns.append(True)
        else:
            returns.append(False)


    return returns



extracandy([4, 2, 1, 1, 2], 1)
