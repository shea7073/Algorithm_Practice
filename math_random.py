import math
import random


value = 4.35

floor = math.floor(value)
ceil = math.ceil(value)
rounded = round(value)
print(floor, ceil, rounded)

pi = math.pi

math.log(100, 10)

r = random.randint(0, 100)
print(r)

random.seed(69)

r2 = random.randint(0, 100)
r3 = random.randint(0, 100)
print(r2, r3)

# Sample with replacement
my_list = list(range(0, 20))
x = random.choice(my_list)
x2 = random.choices(population=my_list, k=5)

# Sample without replacement
x3 = random.sample(population=my_list, k=4)

print(x)
print(x2)
print(x3)
print(my_list)

random.shuffle(my_list)
print(my_list)

print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))