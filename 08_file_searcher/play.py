

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
       current, next = next, next + current
       nums.append(current)

    return nums


for n in fibonacci(100):
    print(n, end=', ')

print()

def fibonacci_co(limit):
   
    current = 0
    next = 1

    while current < limit:
       current, next = next, next + current
       yield current

print('With yield')
for n in fibonacci_co(100):
    print(n, end=', ')

print()