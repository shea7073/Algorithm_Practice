from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]

print(Counter(mylist))

d = defaultdict(lambda: 0)
d["correct"] = 10

print(d["correct"])
print(d["wrong"])

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5,breed="Husky", name="Sam")
print(type(sammy))
print(sammy.age)
print(sammy.name)
print(sammy[0])