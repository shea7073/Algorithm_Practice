try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Operation cannot be done")

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("All Done")

def ask():
    while True:
        try:
            answer = int(input("Input an integer: "))
        except:
            print("An error occured sir")
        else:
            answer = answer ** 2
            print(f"Thank you, your number squared is: {answer}")
            break


ask()
