import time


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
fibonacci(25)
time.time() - start
