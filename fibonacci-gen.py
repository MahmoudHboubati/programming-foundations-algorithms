def fibonacci():
    prev, next = 0, 1
    while True:
        yield next
        prev, next = next, prev+next


fib = fibonacci()

for i in range(10):
    print(next(fib))
