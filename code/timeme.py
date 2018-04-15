from timeit import Timer

fibonacci_test = '[fibonacci(i) for i in range(1, 15)]'

t = Timer(fibonacci_test, 'from fibo2 import fibonacci')
time = t.timeit(number=10000) / 10000.0 * 1000
print('%.2f millisecond/call' % time)
t = Timer(fibonacci_test, 'from fibocache import fibonacci')
time = t.timeit(number=10000) / 10000.0 * 1000
print('%.2f millisecond/call' % time)
