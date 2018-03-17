def fib(n=None):
    """
    Generate the first n elements of the Fibonacci sequence.
    """
    f0, f1 = 1, 1
    count  = 1

    while True:
        if n is not None and count > n:
            return
        yield f0
        f0, f1 = f1, f0 + f1
        count += 1
