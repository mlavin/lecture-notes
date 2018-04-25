def fibonacci():
    current, prev = None, None
    while True:
        if current is None or prev is None:
            yield 1
            current, prev = 1, current
        else:
            current, prev = current + prev, current
            yield current
