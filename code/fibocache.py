import time


def fibonacci(n):
    if hasattr(fibonacci, '_%s' % n):
        return getattr(fibonacci, '_%s' % n)
    if n <= 2:
        value = 1
        setattr(fibonacci, '_%s' % n, value)
        return value
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        setattr(fibonacci, '_%s' % n, value)
        return value


start = time.time()
fibonacci(25)
time.time() - start
