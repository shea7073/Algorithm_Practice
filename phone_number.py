# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string
# of those numbers in the form of a phone number.

def create_phone_number(arr):
    if len(arr) != 10:
        return ValueError('Array Must be 10 digits long!')
    for i in arr:
        if i > 9 or i < 0:
            return ValueError('Phone numbers only except 0-9')
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*arr)



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
