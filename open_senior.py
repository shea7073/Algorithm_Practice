# Output a list determining whether the member will be in the
# senior class or open class. The age should be 55+ and handicap
# greater than 7 to be in senior, will be a list of lists

def open_senior(arr):

    roster = []
    for person in arr:
        if person[0] >= 55 and person[1] > 7:
            roster.append('Senior')
        else:
            roster.append('Open')
    return roster


print(open_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
