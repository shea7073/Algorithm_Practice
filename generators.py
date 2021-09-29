import random

def gensquares(n):
    for number in range(n):
        yield number**2


for x in gensquares(10):
    print(x)


def rand_num(low, high, n):
    for num in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)

s = "hello"

s_iter = iter(s)

print(next(s_iter))

# Search generator comprehension
