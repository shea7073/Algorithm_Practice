import time
import timeit

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

# Current time
start_time = time.time()
# Run code
result = func_one(10000000)

# Record time after code
end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

# Current time
start_time2 = time.time()
# Run code
result2 = func_two(10000000)

# Record time after code
end_time2 = time.time()

elapsed_time2 = end_time2 - start_time2

print(elapsed_time2)



stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
result = timeit.timeit(stmt, setup, number=1000000)
print(result)

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

result2 = timeit.timeit(stmt2, setup2, number=1000000)
print(result2)